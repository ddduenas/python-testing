# 📜 Git Cheat Sheet para Principiantes 🚀
💡 **Git es un sistema de control de versiones que te ayuda a rastrear cambios en el código y colaborar con otros.**

---

## 🔥 1. Configuración Inicial
Antes de empezar, configura tu nombre y correo (solo la primera vez):

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
```

Verifica tu configuración:

```bash
git config --list
```

---

## 📂 2. Crear o Clonar un Repositorio
### Crear un nuevo repositorio:
```bash
git init
```
Esto crea un nuevo repositorio en la carpeta actual.

### Clonar un repositorio existente:
```bash
git clone URL_DEL_REPO
```
Ejemplo:
```bash
git clone https://github.com/tuhermano/proyecto.git
```
Esto crea una copia del proyecto en tu computadora.

---

## 📌 3. Flujo Básico de Trabajo
### Ver el estado del repositorio:
```bash
git status
```
Muestra archivos modificados o no guardados.

### Agregar archivos al área de preparación (staging):
```bash
git add archivo.txt
```
Para agregar todos los archivos:
```bash
git add .
```

### Guardar los cambios con un mensaje:
```bash
git commit -m "Descripción del cambio"
```
🔹 Un commit guarda los cambios localmente, pero aún no los sube al repositorio remoto.

---

## 🌍 4. Trabajando con Repositorios Remotos
### Descargar cambios del servidor (sin mezclarlos con los tuyos):
```bash
git fetch
```
### Descargar y fusionar cambios automáticamente:
```bash
git pull
```
💡 **Usa `git pull` antes de empezar a trabajar para evitar conflictos.**

### Subir cambios al repositorio remoto:
```bash
git push origin main
```
Si estás en otra rama, usa:
```bash
git push origin nombre_de_rama
```

---

## 🔀 5. Trabajando con Ramas (Branches)
### Ver todas las ramas:
```bash
git branch
```
### Crear una nueva rama:
```bash
git branch nombre_rama
```
### Cambiar de rama:
```bash
git checkout nombre_rama
```
O con el nuevo método:
```bash
git switch nombre_rama
```
### Crear y cambiar a una nueva rama en un solo paso:
```bash
git checkout -b nombre_rama
```
O:
```bash
git switch -c nombre_rama
```
### Fusionar una rama con `main`:
```bash
git checkout main
git merge nombre_rama
```

---

## 🚑 6. Solucionar Problemas Comunes
### Deshacer cambios antes de hacer commit:
```bash
git checkout -- archivo.txt
```
### Deshacer un `git add`:
```bash
git reset archivo.txt
```
### Deshacer el último commit (pero mantener los cambios):
```bash
git reset --soft HEAD~1
```
### Revertir el último commit completamente:
```bash
git reset --hard HEAD~1
```
⚠ **¡Cuidado! `--hard` borra los cambios permanentemente.**

---

## 🕵️‍♂️ 7. Ver Historial de Cambios
### Ver commits recientes:
```bash
git log --oneline --graph
```
### Ver cambios en archivos antes del commit:
```bash
git diff
```

---

## 🏆 8. Buenas Prácticas
✔ Siempre usa `git pull` antes de empezar a trabajar.  
✔ Escribe mensajes de commit claros y concisos.  
✔ Usa ramas para trabajar en nuevas funcionalidades.  
✔ Evita hacer `git push` en `main` sin revisar antes.  
✔ No hagas `git commit -m "cambios"` (sé más descriptivo).  

---

Este cheat sheet te ayudará a trabajar mejor con tu hermano y aprender Git sin complicaciones. 🚀 Si necesitas más detalles o ejemplos, dime. ¡Feliz coding! 🖥️✨
