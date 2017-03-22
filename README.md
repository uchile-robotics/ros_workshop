# ros_workshop
Configuración para el workshop sobre ROS

# Crear workspace
```shell
cd # se accede a HOME
mkdir -p workshop_ws/src # se crea una carpeta workshop/src
cd workshop_ws/src # se accede a la nueva carpeta
catkin_init_workspace # se crea un workspace (ws)
cd .. # volvemos root del workspace
catkin_make # compilamos
source devel/setup.bash # se agrega el env del nuevo workspace a la consola (se agregan los nuevos comandos)
echo "source ~/workshop_ws/devel/setup.bash" >> ~/.bashrc # cada vez que se abra la consola se correra el comando
```
# Configuración git
```shell
cd $HOME
git clone https://github.com/uchile-robotics/ros_workshop.git # se descarga el repositorio
cd ros_workshop # se abree el root del repositorio
ln -s $HOME/ros_workshop/ros_workshop/ $HOME/workshop_ws/src/ros_workshop # se crean accesos directos del repositorio en nuestro ws 

# Se debe acceder al ws y compilar el nuevo repo
cd
cd workshop_ws
catkin_make
```

# Crear package
```shell
cd $HOME/workshop_ws/src
catkin_create_pkg test_pkg rospy tf std_msgs std_srvs
```

# Configuración para package con código Python
```shell
roscd test_pkg
mkdir -p src/test_pkg
cd src/test_pkg
touch __init__.py
```

# Nodo Python
```shell
roscd test_pkg/src/test_pkg
touch test.py
chmod +x test.py
```

## Recursos útiles

* [github-gem commands](https://github.com/defunkt/github-gem)
* [maqui installer](https://github.com/uchile-robotics/maqui_system)
