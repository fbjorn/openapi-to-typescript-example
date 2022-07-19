<script lang="ts">
  import { onMount } from "svelte";
  import { Api } from "./lib/Api";
  import type { Task } from "./lib/Api";

  const client = new Api({ baseUrl: "/api" });

  let tasks: Task[] = [];
  let newTaskTitle = "";

  async function refreshTasks() {
    const { ok, data } = await client.tasks.listTasks();
    if (ok) {
      tasks = data.tasks;
    }
  }

  async function createTask() {
    const { ok } = await client.tasks.createTask({ title: newTaskTitle });
    if (ok) {
      await refreshTasks();
      newTaskTitle = "";
    }
  }

  onMount(async () => {
    await refreshTasks();
  });
</script>

<div>
  {#each tasks as task}
    <div>{task.title}</div>
  {/each}

  <form on:submit|preventDefault={createTask}>
    <input bind:value={newTaskTitle} />
    <button type="submit">Add task</button>
  </form>
</div>

<style>
  form {
    display: flex;
    flex-direction: column;
  }
</style>
