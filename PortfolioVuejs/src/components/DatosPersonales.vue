<script setup>
import linkedin from '/src/assets/icons8-linkedin.svg';
import instagram from '/src/assets/icons8-instagram.svg';
import github from '/src/assets/icons8-github.svg';


const tittle = "Melina Aguilar";
const descripcion = "Tecnico Universitario en Programacion";
const residencia = "San Miguel, Tucuman, Argentina";
const presentacion = "Hola, bienvenido a mi portafolio de proyectos. Soy un desarrollador web con experiencia en el desarrollo de aplicaciones web.";
const redesSociales = [
    {id: 1, name: "LinkedIn", src: linkedin, url: 'https://www.linkedin.com/in/melina-aguilar11/'},
    {id: 2, name: "Instagram", src: instagram, url: 'https://www.instagram.com'},
    {id: 3, name: "GitHub", src: github, url: 'https://github.com/Melina-Aguilar'}     
];
const mail = 'aguilarmelinaelizabeth@gmail.com';
</script>

<template>
    <section class="datos-personales">
        <div class="card">
            <div class="perfil-container">
              <img src="/src/assets/fondo8.jpg" alt="Foto de perfil" class="foto-perfil">
              <div class="info-perfil">
               <h1>{{ tittle }}</h1>
                <h2>{{descripcion}}</h2>
               <p>{{presentacion}}</p>
               <ul class="container-lista">
                    <li v-for="red in redesSociales" :key="red.id">
                        <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
                    </li>
               </ul>
               <h3>Contacto: {{mail}}</h3>
               <h4>{{residencia}}</h4>
              </div>
            </div>
          </div>

     </section>
</template>

<style scoped>
h1{
  text-align: center;
  font-size: 4rem;
}

h2{
  text-align: center;
  font-size: 2rem;
  color: rgb(236, 236, 236);
}

p {
  font-size: 1.2rem;
  font-weight: 100;
  margin-bottom: 1rem;
  color:  rgb(236, 236, 236);
}

.card {
  padding: 10px;
  margin: 10px;
  text-align: center;
}
.perfil-container {
  display: flex; /* Usa flexbox para alinear los elementos */
  align-items: center; /* Centra verticalmente */
}

.foto-perfil {
  width: 400px; /* Tamaño de la foto de perfil */
  height: 400px; /* Tamaño de la foto de perfil */
  border-radius: 50%; /* Hacer la imagen circular */
  margin-right: 10px; /* Espacio entre la imagen y el texto */

}


.container-lista {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: left;
}

.icon-redsocial {
  width: 35px; /* Tamaño fijo para los íconos */
  height: 35px; /* Tamaño fijo para los íconos */
  align-items: center;
  background-color: rgb(21, 30, 70);
  border-radius: 50%;
  padding: 0px;
  margin: 5px;
  box-shadow: 0 0 10px hsla(204, 100%, 58%, 0.934);

}

.icon-redsocial:hover{
  background-color:  hsla(204, 100%, 58%, 0.934);
  box-shadow: 0 0 10px rgba(77, 139, 255, 0.815);
}

h3 {
  font-size: 1.2rem;
  font-weight: 500;
}
</style>