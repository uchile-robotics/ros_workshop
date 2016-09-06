# Crear workspace
```
$ cd
$ mkdir -p workshop_ws/src
$ cd workshop_ws/src
$ catkin_init_workspace
$ cd ..
$ catkin_make
$ source devel/setup.bash
$ echo "source ~/workshop_ws/devel/setup.bash" >> ~/.bashrc
```

# Configuración git
```
$ git clone https://github.com/uchile-robotics/ros_workshop.git
$ cd ros_workshop
$ ln -s ~/workshop_ws/bender_workshop ~/ros_workshop/src/bender_workshop
$ # Modificar algún archivo
$ git status
$ git commit -a -m "Primer commit"
```

# Crear package
```
$ cd src
$ catkin_create_pkg test_pkg rospy tf std_msgs std_srvs
```

# Configuración para package con código Python
```
$ roscd test_pkg
$ mkdir -p src/test_pkg
$ cd src/test_pkg
$ touch __init__.py
```

# Nodo Python
```
$ roscd test_pkg/src/test_pkg
$ touch test.py
$ chmod +x test.py
```

