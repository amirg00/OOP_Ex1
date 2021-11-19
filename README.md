## Offline Elevator Scheduling Algorithm: Python 
**Amir Gillette, Ariel University, November 2021.**  



## <a name="table-of-contents"></a> Table of Contents

1. [Algorithm](#Algorithm)
2. [UML Diagram](#UML Diagram)
3. [Results](#Results)
4. [Links](#Links)
5. [Languages and Tools](#Languages and Tools)

<!-- Algorithm  -->

## Algorithm
The algorithm follows Boaz's cmd/simulator conduction. Hence, the first explanation
would focus about how Boaz's cmd/simulator conducts in short. The goal, of course, 
is to have the ability to mimic Boaz's cmd conduction, and thus we could potentially
"foresee" where each elevator is located after a certain call. 
### Boaz's cmd
According to Boaz's cmd, each elevator satisfies one main rule, and it's to 
continue to make the calls with the same direction as the first call, 
without even thinking about new income calls with a diverse direction. When
the income calls with same direction have successfully fulfilled, only
then the elevator can answer a call with a different direction. 

In addition, the cmd is rendering each df time, when in our case
df is 1, meaning that the cmd is rendering each second. However, 
since the calls' time stamps are real number and not integer, then
the cmd would see the incoming call just on the next integer closed
to the time stamp. For example, if we have an incoming call with
time stamp that is "0.785" so the cmd can see it just in time = 1 sec.
This is also true for the arrival time calculations, when we get
a float result, and the cmd would actually tell us that the incoming call
has successfully fulfilled just on the next integer closed to the rounded
call's time stamp adding the calculation also rounded up to it. 


### How then can we extract from that an optimal algorithm?
We can actually always look up for the latest allocated call for a certain 
elevator, following the restriction of Boaz's cmd and rounded calls' time stamps and arrival time.
This looks like a dynamic programming problem, but we aren't
going to build a table and a recursion formula for it, as we need
to follow Boaz's cmd. Therefore, if we're handling each call to
have the optimal elevator, then at the end, when we went over all call with all the elevators,  we would get the optimal 
solution. 

### How does it work? 
We want each elevator to have the structures to save all calls
that are allocated to this specified elevator, and to save a copy
of the calls that are allocated to the elevator, so we can
run our test to find in which elevator we get an optimal allocation. 


Because it's hard to just have one call structure to hold each call, 
since it is inconvenient to approach the time stamps and add to each
call an arrival time calculation, and in general approaching each
call's property. The best solution, at least that I could find, is
to separate the calls towards two lists. One list contains each time stamp
and also the calculation for the evaluated arrival time for each call, which
is the time that the call is done as if we had put it in Boaz's simulator/cmd.
The second list has a call's source and destination, such that we can
simulate what would have happened in Boaz's simulator if we
allocate a certain call to a certain elevator. 

In addition, we want simultaneously to update each elevator's lists for each incoming call,
so we could keep a track of which times belong to which source and destination. But, there
are some obstacles in that way. We do know that we should check if a call
can be answered by an elevator that on the way to complete a call, and we want
to check how to calculate the new timestamps and arrival time if needed, those points are well detailed 
in the project documentations. 



<!-- UML Diagram  -->

## UML Diagram 
![Domain model in PlantUML](http://www.plantuml.com/plantuml/svg/RLFTJjmy4BttK-H3tyNIPOdW4gaI1T7UL4Bg2rZ6dYGk_eayOw15l7l7tYGBMIvs8vzpVCPpnhv6KecoTqByz__DZzlxd_U_lfuyEAKVJnYoGRjie1c8HhngswIUptjBGtx824d7G13eN4VVFg0UdbNwsuvijgC1F63h5HAaTbfLrzrZiFr0xsIxz_XvmOKGtrmV4nVopMxtfRbLpk4AkydM6HjwePr2R1RoLMnraJTNZRD8OWiEdXJ5T41OsDkWdFmeB2jfWu4NXcnWHB6fzCg6pMcbTNQAGERHb0zP3vl5_Qmf-rbd0q8YsTc4LEc5yP1ws1UT2BmuQmp_y9A_bujG6ICfIWZcdK5H5XCRQcNvpDrMCpwSU1Dp7ZMSk-bKOafd9ZcSpZgGGNdW9f5IDVpkOanpqrwzV5WVv_SROv09b86qMUnEnTjShOxhQ0uwZdzax6IAEPXrzFZqYU5s2Zfc6ZDjYgYmJ1myQXP8oezOXpI0VjmJ319iCEapmmBc68oQiQduflxNmIBj8VcaN8PYj3IpHCdzM3DdWYD0MNGkAjhFf5jb-17GBkB-nXnsnH722gglyGYBumfIY57RsifnnYketfKQqAUOB5iMeWUIbUnYgZw7_4eYvIdK-xMyjZcbmhoAfjdMrrB4ToyNLLg0ISJGwo5OObUfsAXYuXg2oTxz0m00)


## Results

Here is the results we got, for the compatible building to the calls.

|   Building  | Case | Total Waiting Time | Average Waiting Time Per Call | UnCompleted Calls    | Certificate |
|:--------:|:--------:|:--------:|:--------:| :--------:|:--------:|
| B1 |  Calls_a   |   11292.0   |   112.92  | 0|  -259939903|
| B2 |  Calls_a   |   5073.0   |   50.73  | 0|  -305742041|
| B3 |   Calls_a  |  3030.0    | 30.3    | 0|-509550933  |
| B3 |   Calls_b  |   532235.9081919998   | 532.2359081919998    | 129| -1976019960 |
|  B3|   Calls_c  |    564201.2208050041  |  564.2012208050041   | 101|  -1820076381|
| B3 |   Calls_d  |   536300.4860640028   |  536.3004860640028   | 104| -1983605446 |
| B4 |  Calls_a   |  1611.0    |   16.11  | 0| -456718175 |
| B4 |  Calls_b   |   187357.22828799993   |  187.35722828799993   | 6| -1041127694 |
| B4 |  Calls_c   |   184178.76122   |   184.17876121999998  |4 | -1034702736 |
| B4 |  Calls_d   |  183088.874732    |  183.088874732   |2 | -1037639284 |
| B5 |  Calls_a   |   1065.0   |  10.65   | 0| -444400081 |
| B5 |  Calls_b   |   31722.0   |  31.722   |0 | -504524452 |
|  B5|  Calls_c   |    31956.0  |  31.956   |0 | -504524452 |
|  B5|  Calls_d   |  31645.0    |  31.645   | 0| -504524452 |




<!-- Links  -->
## Links
Well, I took inspiration from the following article: 
* [On-line Algorithms versus Off-line Algorithms for the Elevator](https://studylib.net/doc/7878746/on-line-algorithms-versus-off-line-algorithms-for-the-ele...)

There is a link for the README of the previous assignment:
* [Ex0_Readme](https://docs.google.com/document/d/1mpZujTy5iBqluBIg-lFaehn_-DZAAC5blGZ5gd_aUQ0/edit)

* Note: this readme is written in HEBREW. 


<!-- Languages and Tools -->

## Languages and Tools

  <div align="center">
  
 <code><img height="40"  src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code> 
 <code><img height="40" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png"></code>
 <code><img height="40" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/terminal/terminal.png"></code>
  </div>


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Python](https://www.python.org/)
* [Git](https://git-scm.com/)
* [Git-scm](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
