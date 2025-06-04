# Virtualizacion_AySO

Proyecto de Virtualización con VirtualBox y Ubuntu Desktop


🚀 Descripción del Proyecto

Este proyecto práctico tiene como objetivo principal la implementación y configuración de un entorno virtualizado utilizando **Oracle VirtualBox**. Se detallan los pasos para crear una máquina virtual (VM) con **Ubuntu Desktop 24.04.2 LTS** y configurar en ella las herramientas necesarias para correr programas en Python.. Además, se aborda brevemente la virtualización ligera con contenedores (**Docker**) para comprender las diferencias entre ambos enfoques.

El propósito es adquirir experiencia práctica en la virtualización, un pilar fundamental en la administración de sistemas y el desarrollo de software moderno.

✨ Tecnologías Utilizadas

Oracle VirtualBox: Hipervisor Tipo 2 para la creación y gestión de VMs.
Ubuntu Desktop 24.04.2 LTS: Sistema operativo invitado.
Apache2: Servidor web HTTP.
Python3 & pip3: Para la ejecución de scripts en la VM (ej. cálculo de promedios).

🛠️ Configuración y Uso

Prerrequisitos

 Un sistema operativo anfitrión (Host) compatible con VirtualBox (ej. Windows, macOS, Linux).
 Acceso a internet para descargar VirtualBox e imágenes ISO.

 Pasos de Configuración (Resumen)

1.  Instalar VirtualBox: Descargar e instalar Oracle VirtualBox en el sistema anfitrión.
2.  Descargar Ubuntu: Obtener la imagen ISO de Ubuntu Desktop 24.04.2 LTS desde el sitio oficial de Ubuntu.
3.  Crear Máquina Virtual:
     Abrir VirtualBox y crear una nueva VM.
     Asignar 2 GB de RAM y un disco duro virtual de 50 GB.
     Configurar el adaptador de red de la VM en **Modo Puente (Bridged Adapter)** para permitir el acceso directo desde la red local.
4.  Instalar Ubuntu Desktop 24.04.2 LTS: Iniciar la VM con la imagen ISO montada y seguir el proceso de instalación mínima.
5.  Instalar y Configurar Apache:
     Actualizar paquetes: `sudo apt update && sudo apt upgrade -y`
     Instalar Apache2: `sudo apt install apache2 -y`
     Habilitar firewall: `sudo ufw allow 'Apache'`
6. Instalar Python y pip (Opcional, para desarrollo):
    Verificar Python: `python3 --version`
    Instalar/Actualizar Python: `sudo apt update && sudo apt install python3 -y`
Instalar pip: `sudo apt install python3-pip -y`

Verificación del Servidor Web

Para verificar que el servidor Apache esté funcionando:

1.  Obtén la dirección IP de tu VM Ubuntu Desktop 24.04.2 LTS (ej. usando `ip a` en la terminal de la VM).
2.  Desde un navegador web en tu sistema anfitrión o en otro dispositivo de la misma red, ingresa la dirección IP de la VM.
3.  Deberías ver la página por defecto de Apache ("It works!").

🚧 Dificultades Encontradas

Dependencia de Microsoft Visual C++ 2019:** Mensaje de requisito durante la descarga de VirtualBox, aunque la instalación principal se completó sin problemas.
Distribución de Teclado en la Terminal de la VM:** Diferencias en la ubicación de caracteres (`=`, `:`) en la terminal de Ubuntu Server respecto al teclado físico, lo que requirió adaptación durante la escritura de código.

👥 Alumnos

 Lerda Fernando – fglerda@gmail.com
 Lopez Joana – Jl105658@gmail.com

 📽️ link al video explicativo:
 https://youtu.be/2DWsx8Q81NU

🗓️ Fecha de Entrega

5 de junio de 2025

---
