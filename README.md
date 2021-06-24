<pre>
           _____   ____  _____         _____           _                 
     /\   |  __ \ / __ \|  __ \       / ____|         | |                
    /  \  | |__) | |  | | |__) |_____| |     _ __ __ _| | _____ _ __ ___ 
   / /\ \ |  ___/| |  | |  ___/______| |    | '__/ _` | |/ / _ \ '__/ __|
  / ____ \| |    | |__| | |          | |____| | | (_| |   <  __/ |  \__ \
 /_/    \_\_|     \____/|_|           \_____||_|  \__,_|_|\_\___|_|  |___/
 
</pre>
</br>
</br>

An APOP passwod bruteforce finder using dictionary like rock-you

you need to install tkinter for the purpose of the app 

after capturing a suceful sniffing connections trought APOP you need to retreve 2 thing 

</br>
</br>

- the process-ID.clock + hostname
 
  - the process-ID.clock + hostname is in the first APOP packet 
  
  - ex: <1755.1.5f403625.BcWGgpKzUPRC8vscWn0wuA==@vps-7e2f5a72>

</br>
</br>


- the MD5 hash value of the stamp + password 

  - the hash is in the Post Office Protocol in the APOP bsmith sections
  
  - ex: 4ddd4137b84ff2db7291b568289717f0

</br>
</br>



after finding this two parameter put them in the named case , select your brute-force dictionary and whait 

write by biero el corridor for APOP challenge of root me 


