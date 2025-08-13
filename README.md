# 👾 Space Invaders

🎮 Proyecto de desarrollo de un videojuego clásico tipo arcade.



#### 📚 Curso : Introduccion a la programación

---

## 🧠 Descripción
Este proyecto implementa una versión moderna del clásico juego Space Invaders utilizando Python y Pygame. El jugador controla una nave espacial que debe eliminar oleadas de enemigos que caen antes de que lleguen al borde inferior de la pantalla. El juego incluye animaciones, efectos de sonido, y un sistema de puntuación .

---

## 🛠️ Requisitos
- Sistema operativo: Windows 
- Python 3

---

## 📦 Descarga e instalación
1. Descargar Python 3
2. Descargar e instalar la libreria de pygame
    ```bash
   pip install pygame 
   ```  
3. Descargue el repositorio:
   ```bash
   git clone https://github.com/usuario/space-invaders.git

---
## :alien: ¿ Cómo ejecutar? :alien:
Ejecute el main.py con su ide de preferencia , o bien abra la consola de comandos (cmd) dirijase al directorio donde descargo el repositorio, y ejecute el siguiente comando 


 ```bash
python main.py 
 ```
---
## Principales Características  :trophy:
### Puntajes
- Al iniciar el juego se observara la siguiente pantalla, se le solicita su nombre de jugador , el cual sera registrado para los altos puntajes
 > :alien: NOTA: se registraran solo si obtiene un puntaje mayor a los ya registrados :alien:
<img width="585" height="401" alt="image" src="https://github.com/user-attachments/assets/70d738aa-b197-4255-96bc-03dbcb21a7a7" />

### Enemigos :alien:

<img width="26" height="48" alt="image" src="https://github.com/user-attachments/assets/db0d1c37-c3c5-4536-9e43-04b0fff7d508" />

Los enemigos son alines que descienden en fila y columa, disparan aleatoriamente al jugador , por cada alien eliminado se genera puntaje
> existe otro tipo de enemigo especial, aplastadores, caeran de la esquina izquierda o derecha de la pantalla y dispararan horizontalmente al jugador 👾
---
### jugador :rocket:
#### Tu eres un astronauta en una nave espacial , ¡Sobrevive!
##### principales caracteristicas:
-El jugador pose movimiento horizontal y es capaz de utilizar la "maxima propulsion" por unos breves segundos, evitando los disparos de los aliens de las esquinas
> Pulsar espacio para utilizar la máxima propulsion :rocket:
- El jugador puede disparar a los aliens, presione el click izquierdo del mouse para disparar :boom:
---
### :video_game: niveles :video_game:
Se cuentan con 3 niveles , cada uno con su dificultad basada en la velocidad de caida de los aliens, y su frecuencia de disparo, se describen los niveles
1. la velocidad normal de descenso de los aliens.
2. los aliens se mueven y disparan más rápido, ahora en ocasiones caera un alien por la izquierda o la derecha de vez en cuando.
3.  la velocidad de disparo y movimiento es duplicada, asi como la frecuencia de aparición de los enemigos aplastadores. 

---
## :notebook: Notas adicionales :notebook:
Actualmente el juego no recibe soporte u actualizaciones.
