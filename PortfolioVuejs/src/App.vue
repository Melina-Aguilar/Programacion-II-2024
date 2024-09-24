<script setup> // setup: indica que se va a ejecutar solamente el codigo que se encuentra dentro de este script
  import NavBar from './components/icons/NavBar.vue';
  import DatosPersonales from './components/DatosPersonales.vue';
  import Educacion from './components/Educacion.vue';
</script>

<template>

  <header>
    <!-- Barra de Navegacion -->
     <NavBar />

    <!-- Componente Datos Persoanles-->
      <DatosPersonales />
  </header>

  <main>
    <!-- El estilo css de section se encuentra en base.css-->
      <section id="educacion"><h2>Educacion - Cursos</h2>
      <Educacion/>
      </section>
      <section id="experiencia"><h2>Experiencia</h2></section>
      <section id="proyectos"><h2>Proyectos</h2></section>
      <section id="habilidades"><h2>Habilidades</h2></section>
      <section id="intereses"><h2>Intereses</h2></section>
  </main>
  

</template>

<style scoped>

</style>
