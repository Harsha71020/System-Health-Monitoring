#  System  Health  Monitoring  Dashboard




This  project  provides  a  system  health  monitoring  dashboard  that  tracks  CPU,  memory,  and  disk  usage.  It  uses  Python  to  collect  system  metrics,  stores  them  in  an  SQLite  database,  and  visualizes  them  using  a  web  interface  built  with  Flask  and  HTML.




##  Features




* Metric  Collection:  Gathers  CPU,  memory,  and  disk  usage  using  the  `psutil`  library.




* Data  Storage:  Stores  collected  metrics  in  an  SQLite  database  (`system_metrics.db`).




* Web  Visualization:  Presents  a  real-time  view  of  system  metrics  through  a  web  dashboard.




* Real-time  Updates:  The  dashboard  updates  dynamically  to  show  the  latest  system  statistics.




* Alerting:  Highlights  high  CPU,  memory,  or  disk  usage  with  color-coded  cells  and  pulse  animations.




##  Files




* `app.py`:  Flask  application  to  serve  the  dashboard  and  fetch  metrics  from  the  database.




* `monitor.py`:  Python  script  to  collect  system  metrics  and  log  them  into  the  database.




* `view_data.py`:  Python  script  to  view  metrics  directly  from  the  database  in  the  console.




* `dashboard.html`:  HTML  template  for  the  web  dashboard,  displaying  system  metrics  in  a  table.




* `view_metrics.sql`:  SQL  query  to  fetch  the  last  10  logged  system  metrics.




* `system_metrics.db`:  SQLite  database  file  (will  be  created  after  running  `monitor.py`).




* `README.md`:  Documentation  for  the  project.




##  Setup  Instructions




1.  Prerequisites:




    * Python  3.x




    * `psutil`  library  (`pip  install  psutil`)




    * Flask  (`pip  install  Flask`)




2.  Running  the  Application:




    * First,  run  `monitor.py`  to  start  logging  system  metrics  to  the  database:
        ```bash
        python  monitor.py
        ```




    * Then,  run  `app.py`  to  start  the  Flask  web  application:
        ```bash
        python  app.py
        ```




    * Open  your  web  browser  and  navigate  to  `http://127.0.0.1:5000/`  to  view  the  dashboard.




3.  Viewing  Metrics  from  the  Command  Line  (Optional):




    * Run  `view_data.py`  to  display  the  metrics  in  your  terminal:
        ```bash
        python  view_data.py
        ```




##  Database




The  `system_metrics.db`  database  stores  the  system  metrics  with  the  following  schema:




* `timestamp`  (TEXT):  Timestamp  of  when  the  metrics  were  recorded.




* `cpu`  (REAL):  CPU  usage  percentage.




* `memory`  (REAL):  Memory  usage  percentage.




* `disk`  (REAL):  Disk  usage  percentage.




##  Customization




* Dashboard  Styling:  You  can  customize  the  appearance  of  the  dashboard  by  modifying  the  CSS  styles  in  `dashboard.html`.




* Alert  Thresholds:  Adjust  the  threshold  for  high  CPU,  memory,  and  disk  usage  in  `dashboard.html`  by  changing  the  values  in  the  `if  row[1]|int  >  80`  conditions.




* Metric  Logging  Interval:  Modify  the  logging  interval  in  `monitor.py`  by  changing  the  `time.sleep(60)`  value  (in  seconds).




* Database  Queries:  Modify  the  SQL  queries  in  `app.py`  or  use  `view_metrics.sql`  to  retrieve  specific  data  from  the  database.




##  Notes




* Ensure  that  `monitor.py`  is  running  in  the  background  to  continuously  log  system  metrics.




* The  dashboard  displays  the  last  50  metrics  recorded.




* This  project  provides  a  basic  monitoring  solution.  For  more  advanced  monitoring,  consider  using  dedicated  monitoring  tools.



##  Output



![Screenshot 2025-05-18 234026](https://github.com/user-attachments/assets/016275bc-bcef-4084-b14e-91968f0be747)
