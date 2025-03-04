<template>
  <div class="login-container">
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label>用户名</label>
        <input v-model="username" type="text" required />
      </div>
      <div class="form-group">
        <label>密码</label>
        <input v-model="password" type="password" required />
      </div>
      <button type="submit">登录</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const username = ref('')
const password = ref('')

const handleSubmit = async () => {
  try {
    const response = await axios.post('http://localhost:8001/auth/login', {
      username: username.value,
      password: password.value
    })
    alert(response.data.message)
  } catch (error) {
    alert('登录失败')
  }
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 2rem auto;
  padding: 2rem;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}
.form-group {
  margin-bottom: 1rem;
}
input {
  width: 100%;
  padding: 0.5rem;
  margin-top: 0.5rem;
}
button {
  width: 100%;
  padding: 0.75rem;
  background: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}
</style>