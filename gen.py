import json, random, time, socket, platform

timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")



f = open("./README.md", "w")

f.write(f'''

 <p align="left"> <img src="https://komarev.com/ghpvc/?username=xtenzq&label=Profile%20views&color=0e75b6&style=flat" alt="xtenzq" /> </p>  

 <p> <a href="https://twitter.com/xtenzq" target="blank"><img align="center" src="https://iconape.com/wp-content/png_logo_vector/drone.png" height="50px" width="50px" />  </a>  .  .
 <a href="https://youtube.com" target="blank"><img align="center" src="https://iconape.com/wp-content/files/cm/286303/svg/youtube-icon-logo-logo-icon-png-svg.png" height="50px" width="70px" />  </a>  .  .
 <a href="https://twitter.com/xtenzq" target="blank"><img align="center" src="https://image.flaticon.com/icons/png/128/1409/1409937.png" height="50px" width="50px" /></a> </p>  
  <p align="left"> <img src="https://www.pngarts.com/files/12/Blue-Discord-Logo-Icon-PNG-Picture.png" height="50%" width="50%"  /> </p>  


 ```bash

 {timestr}

 ```


 ```bash

 Host Name : {socket.gethostname()}

 platform  : {platform.platform()}

 Ip Local  : {socket.gethostbyname(socket.gethostname())}

 ```



 ''')

f.close()
