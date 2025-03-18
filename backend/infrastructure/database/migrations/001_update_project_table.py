import aiosqlite
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

async def migrate_project_table(db_path: str):
    backup_db_path = str(Path(db_path).with_suffix('.backup.db'))
    
    try:
        # 1. Create backup
        async with aiosqlite.connect(db_path) as conn:
            await conn.backup(backup_db_path)
        
        # 2. Get existing data
        async with aiosqlite.connect(db_path) as conn:
            cursor = await conn.execute('SELECT * FROM project')
            existing_data = await cursor.fetchall()
            column_names = [description[0] for description in cursor.description]
        
        # 3. Drop and recreate table with new schema
        async with aiosqlite.connect(db_path) as conn:
            await conn.execute('DROP TABLE IF EXISTS project')
            
            # Create new table with updated schema
            await conn.execute('''
                CREATE TABLE IF NOT EXISTS project (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    project_name VARCHAR(100) NOT NULL,
                    description TEXT,
                    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    create_by VARCHAR(50),
                    update_by VARCHAR(50)
                )
            ''')
            
            # 4. Migrate existing data
            if existing_data:
                # Map old data to new schema
                for row in existing_data:
                    data_dict = dict(zip(column_names, row))
                    
                    # Adjust column names if needed
                    insert_data = {
                        'project_name': data_dict.get('name', '') or data_dict.get('project_name', ''),
                        'description': data_dict.get('description', ''),
                        'create_time': data_dict.get('created_at', '') or data_dict.get('create_time', ''),
                        'update_time': data_dict.get('updated_at', '') or data_dict.get('update_time', ''),
                        'create_by': data_dict.get('creator_id', '') or data_dict.get('create_by', ''),
                        'update_by': data_dict.get('update_by', '')
                    }
                    
                    await conn.execute('''
                        INSERT INTO project (
                            project_name, description, create_time, update_time, create_by, update_by
                        ) VALUES (?, ?, ?, ?, ?, ?)
                    ''', (
                        insert_data['project_name'],
                        insert_data['description'],
                        insert_data['create_time'],
                        insert_data['update_time'],
                        insert_data['create_by'],
                        insert_data['update_by']
                    ))
            
            await conn.commit()
            
        logger.info('Project table migration completed successfully')
        return True
        
    except Exception as e:
        logger.error(f'Migration failed: {str(e)}')
        # Restore from backup if migration fails
        try:
            async with aiosqlite.connect(backup_db_path) as backup_conn:
                async with aiosqlite.connect(db_path) as conn:
                    await backup_conn.backup(db_path)
            logger.info('Database restored from backup')
        except Exception as restore_error:
            logger.error(f'Failed to restore backup: {str(restore_error)}')
        return False
    finally:
        # Clean up backup file
        try:
            Path(backup_db_path).unlink(missing_ok=True)
        except Exception as e:
            logger.error(f'Failed to remove backup file: {str(e)}')