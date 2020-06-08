import random
from random import randrange

#Welcoming intro
print("Mamy 105 R.N.E., 6 rok panowania boskiego Marcusa Ulpiusa,zwanego Trajanem.")
print("Cesarstwo Rzymskie osiagnelo najwiekszy zasieg terytorialny wswoich dziejach")
print("\n")

#asking player if he/she wants to play the game
startQuestion=input("Czy chcesz zostac mianowany namiestnikiem Rzymskiej kolonii w cesarstwie Zachodnio Rzymskim?\n").lower()
if startQuestion!="tak":
    print("Do nastepnego roku")
    quit()
    
else:
    name=input("Twoje imiona: ")
    age=int(input("Wiek: "))
    if age<18:
        print("Jestes za mlody!")
        quit()
    elif age>96:
        print("Niestety boski Marcus Ulpius uwaza, ze jestes zbyt stary i niedolezny.")
        quit()
    else:
        print("\n")
        print("Zostales mianowany, powodzenia.")
        
#intro if the player has been chosen to run the Colony
print("\nTwoj administrator Gallius przesyla Ci regularne sprawozdania.")
print("Do Ciebie naleza decyzje.")
print("\nTwoj urzad trwa 10 lat.")
print("\n")

#game starting parameters
start_colony_size=(randrange(50,150))
start_acres=(randrange(1000,2000))
start_grain=(randrange(2500,3500))
died=0
year_of_rule=1
seed=0

colony_size=start_colony_size #population of the colony
grain=start_grain #grain the colony has
acres=start_acres #area of the colony
seeds=seed #area you want to seed
alive=True

population_list=[]
death_list=[]
grain_list=[]
acres_list=[]

#main game loop
while alive:
    #stats for the year/beginning of each loop
    rats_ate=[0,0,0,(randrange(0,1000))]
    eaten_by_rats=random.choice(rats_ate)
    immigrants=(randrange(0,30))
    cost_of_acre=(randrange(17,28))
    harvestlist=[1,2,2,3,3,3,4,4,4,4,5,5,5,6,6,7]
    harvest=random.choice(harvestlist)
    
    #lists for statistics of colony performance

    population_list.append(colony_size)
    death_list.append(died)
    grain_list.append(grain)
    acres_list.append(acres)
    
    #summary of ruling after 10 years
    year_of_rule_list=[11,21,31,41,51,61,71,81,91,101,111,121,131,141,151,161,171,181,191,201]
    if year_of_rule in year_of_rule_list:
        rule_points_ten_years=[]
        if population_list[-11]<=population_list[-1]:
            rule_points_ten_years.append(1)
        if sum(death_list[-11:-1])==0:
            rule_points_ten_years.append(1)
        if grain_list[-11]<=grain_list[-1]:
            rule_points_ten_years.append(1)
        if acres_list[-11]<=acres_list[-1]:
            rule_points_ten_years.append(1)
        summary_of_rule_points_ten_years=sum(rule_points_ten_years)
        
        died_in_10_years=sum(death_list[-10:-1])
        print("\nW ciagu Twojego 10 letniego panowania zmarlo z Twojej winy",died_in_10_years,  "ludzi, ")
        percentage=round(((died_in_10_years)/(population_list[-10])*100),2)
        print("to jest",percentage,"% mieszkancow.")
        land_per_person_before=((acres_list[-10])//(population_list[-10]))
        land_per_person_now=((acres_list[-1])//(population_list[-1]))
        print("Na poczatku kazdy mial",land_per_person_before, "morg ziemi, teraz kazdy ma",land_per_person_now," morg.")
        
        if summary_of_rule_points_ten_years>=3:
            print("Za Twojego panowania kolonia przezyla okres wspanialego rozkwitu.")
            print("Mieszkancy pragna, abys byl namiestnikiem przez nastepne 10 lat.")
            ten_year_question=input("Czy zgadzasz sie?\n").lower()
            if ten_year_question !="tak":
                print("Dziekujemy za sluzbe.")
                quit()
        
        if summary_of_rule_points_ten_years==2:
            print("Twoje rzady mogly byc lepsze ale nie byly zle. Czesc Twoich ludzi chce Cie ponownie jako namiestnika.")
            ten_year_question=input("Czy zgadzasz sie?\n").lower()
            if ten_year_question !="tak":
                print("Dziekujemy za sluzbe.")
                quit()
        
        if summary_of_rule_points_ten_years==1:
            print("Twoje bezlitosne rzady przypominaja nerona. Mieszkancy ktorzy przezyli nienawidza Twojego szczegolnego stylu wladzy.")
            quit()
        
        if summary_of_rule_points_ten_years==0:
            print("Za tak zle rzady zdjeto Cie z urzedu i wtracono do wiezienia.")
            quit()
        print("-------------------")
        print("-------------------")
    
    #results of the year
    print("W",year_of_rule,"roku zmarlo",died,"ludzi i",immigrants,"przybylo do kolonii.")
    colony_size=((colony_size+immigrants)-died)
    print("Kolonia ma",colony_size,"mieszkancow i",acres,"morg powierzchni.")
    print("Zbiory wyniosly",harvest,"korcow zboza z morgi.")
    grain=(harvest*seeds)+grain
    print("Szczury zjadly",eaten_by_rats,"korcow zboza.")
    grain=grain-eaten_by_rats
    if grain<0:
        grain=0
    print("W magazynach masz",grain,"korcow zboza.")
    print("Ziemia kosztuje w tym roku",cost_of_acre,"korcow za morge.")
    
    #define if you want to buy more land
    buy=int(input("Ile morg mam kupic?: "))
    while grain<=0:
        grain=0
        break
    while grain<(buy*cost_of_acre):
        buy=0
        print("Zastanow sie,masz tylko",grain,"korcow zboza.")
        while grain<=0:
            grain=0
            buy=0
        buy=int(input("Ile morg mam kupic?: "))
        if grain>(buy*cost_of_acre):
            continue
        continue
    grain=grain-(buy*cost_of_acre)
    acres=acres+buy
    
    #define if you want to sell land
    sell=int(input("Ile morg mam sprzedac?: "))
    
    while acres<sell:
        sell=0
        print("Zastanow sie,masz tylko",acres,"morg powierzchni.")
        sell=int(input("Ile morg mam sprzedac?: "))
        if sell<=acres:
              break
    grain=grain+(sell*cost_of_acre)
    acres=acres-sell
    
    #provide grain to feed people
    print("Bedziesz mial w magazynach",grain,"korcow zboza.")
    food_for_people=int(input("Ile korcow przeznaczyc na zywnosc?: "))
    while food_for_people>grain:
        print("Zastanow sie,masz tylko",grain,"korcow zboza.")
        food_for_people=int(input("Ile korcow przeznaczyc na zywnosc?: "))
        continue
    grain=grain-food_for_people
    if grain<=0:
        grain=0
        
    #area you want to seed
    print("Bedziesz mial w magazynach",grain,"korcow zboza.")
    seeds=int(input("Ile morg obsiac?: "))
    while seeds>acres:
        print("Zastanow sie, masz tylko",acres,"morg ziemi.")
        seeds=int(input("Ile morg obsiac?: "))
        continue
    
    while (seeds*2)>grain:
        print("Zastanow sie,masz tylko",grain,"korcow zboza.")
        seeds=int(input("Ile morg obsiac?: "))
        continue
    grain=grain-(seeds*2)
    
    #calculates how much land people of colony can seed
    how_much_seed=(colony_size*20)        
    while how_much_seed<seeds:
        print("Ale masz tylko",colony_size,"ludzi do pracy w polu,ktorzy moga obsiac",how_much_seed,"morg.")
        seeds=int(input("Ile morg obsiac?: "))
        continue
    
    #calculates howmuch foodpeopleofyour colony need
    food_required=colony_size*20
    if food_required>(food_for_people):
        died=((food_required)-(food_for_people))//20
    else:
        died=0
    
    print("-------------------")
    print("-------------------")
    
    #Summary of the year after you made your decisions
    year_of_rule=year_of_rule+1
    if died>(colony_size//2):
        print("Zmarlo Ci",died,"ludzi.")
        print("Zrozpaczeni mieszkancy kolonii pala dom administratora\na jego samego wieszaja na galezi.\nNastepnie pladruja i grabia magazyny.")
        print("Za doprowadzenie do tego swoimi rzadami\nzostajesz odwolany i wtracony do wiezienia.")
        quit()
    
    #disease
    disease=randrange(1,4)
    if disease==1:
        print("Straszna epidemia nawiedzila Twoja kolonie.")
        print("Polowa ludnosci zmarla.")
        print("\n")
        colony_size=(colony_size//2)
    
    #age of player after the year
    age=age+1
    
    #performance after 10 years of rule or at death
    rule_points_death=[]
    if population_list[0]<=population_list[-1]:
        rule_points_death.append(1)
    if death_list[0]<=death_list[-1]:
        rule_points_death.append(1)
    if grain_list[0]<=grain_list[-1]:
        rule_points_death.append(1)
    if acres_list[0]<=acres_list[-1]:
        rule_points_death.append(1)
    summary_of_rule_points_death=sum(rule_points_death)
    
    #death of player
    if 18<=age<=24:
        age18to24=randrange(1,1908)
        if age18to24==1:
            print("W",year_of_rule,"roku Twoich rzadow umierasz nagle.")
            if summary_of_rule_points_death>3:
                print("Mieszkancy kolonii szczerze Cie oplakuja, stawiaja Ci swiatynie,liczne pomniki i przekazuja pamiec o Tobie z pokolenia na pokolenie.")
            elif summary_of_rule_points_death==2:    
                print("Mieszkancy kolonii szczerze Cie oplakuja.")
            elif summary_of_rule_points_death==1:
                print("Mieszkancy kolonii oddychaja z ulga.")
            elif summary_of_rule_points_death==0:
                print("Mieszkancy kolonii skladaja dziekczyne ofiary bogom, niszcza Twoj grobowiec a zwloki wyrzucaja do rzeki.")
            alive=False
            quit()
    if 25<=age<=34:
        age25to34=randrange(1,1215)
        if age25to34==1:
            print("W",year_of_rule,"roku Twoich rzadow umierasz nagle.")
            if summary_of_rule_points_death>3:
                print("Mieszkancy kolonii szczerze Cie oplakuja, stawiaja Ci swiatynie,liczne pomniki i przekazuja pamiec o Tobie z pokolenia na pokolenie.")
            elif summary_of_rule_points_death==2:    
                print("Mieszkancy kolonii szczerze Cie oplakuja.")
            elif summary_of_rule_points_death==1:
                print("Mieszkancy kolonii oddychaja z ulga.")
            elif summary_of_rule_points_death==0:
                print("Mieszkancy kolonii skladaja dziekczyne ofiary bogom, niszcza Twoj grobowiec a zwloki wyrzucaja do rzeki.")
            alive=False
            quit()
    if 35<=age<=44:
        age35to44=randrange(1,663)
        if age35to44==1:
            print("W",year_of_rule,"roku Twoich rzadow umierasz nagle.")
            if summary_of_rule_points_death>3:
                print("Mieszkancy kolonii szczerze Cie oplakuja, stawiaja Ci swiatynie,liczne pomniki i przekazuja pamiec o Tobie z pokolenia na pokolenie.")
            elif summary_of_rule_points_death==2:    
                print("Mieszkancy kolonii szczerze Cie oplakuja.")
            elif summary_of_rule_points_death==1:
                print("Mieszkancy kolonii oddychaja z ulga.")
            elif summary_of_rule_points_death==0:
                print("Mieszkancy kolonii skladaja dziekczyne ofiary bogom, niszcza Twoj grobowiec a zwloki wyrzucaja do rzeki.")
            alive=False
            quit()
    if 45<=age<=54:
        age45to54=randrange(1,279)
        if age45to54==1:
            print("W",year_of_rule,"roku Twoich rzadow umierasz nagle.")
            if summary_of_rule_points_death>3:
                print("Mieszkancy kolonii szczerze Cie oplakuja, stawiaja Ci swiatynie,liczne pomniki i przekazuja pamiec o Tobie z pokolenia na pokolenie.")
            elif summary_of_rule_points_death==2:    
                print("Mieszkancy kolonii szczerze Cie oplakuja.")
            elif summary_of_rule_points_death==1:
                print("Mieszkancy kolonii oddychaja z ulga.")
            elif summary_of_rule_points_death==0:
                print("Mieszkancy kolonii skladaja dziekczyne ofiary bogom, niszcza Twoj grobowiec a zwloki wyrzucaja do rzeki.")
            alive=False
            quit()
    if 55<=age<=64:
        age55to64=randrange(1,112)
        if age55to64==1:
            print("W",year_of_rule,"roku Twoich rzadow umierasz nagle.")
            if summary_of_rule_points_death>3:
                print("Mieszkancy kolonii szczerze Cie oplakuja, stawiaja Ci swiatynie,liczne pomniki i przekazuja pamiec o Tobie z pokolenia na pokolenie.")
            elif summary_of_rule_points_death==2:    
                print("Mieszkancy kolonii szczerze Cie oplakuja.")
            elif summary_of_rule_points_death==1:
                print("Mieszkancy kolonii oddychaja z ulga.")
            elif summary_of_rule_points_death==0:
                print("Mieszkancy kolonii skladaja dziekczyne ofiary bogom, niszcza Twoj grobowiec a zwloki wyrzucaja do rzeki.")
            alive=False
            quit()
    if 65<=age<=74:
        age65to74=randrange(1,42)
        if age65to74==1:
            print("W",year_of_rule,"roku Twoich rzadow umierasz nagle.")
            if summary_of_rule_points_death>3:
                print("Mieszkancy kolonii szczerze Cie oplakuja, stawiaja Ci swiatynie,liczne pomniki i przekazuja pamiec o Tobie z pokolenia na pokolenie.")
            elif summary_of_rule_points_death==2:    
                print("Mieszkancy kolonii szczerze Cie oplakuja.")
            elif summary_of_rule_points_death==1:
                print("Mieszkancy kolonii oddychaja z ulga.")
            elif summary_of_rule_points_death==0:
                print("Mieszkancy kolonii skladaja dziekczyne ofiary bogom, niszcza Twoj grobowiec a zwloki wyrzucaja do rzeki.")
            alive=False
            quit()
    if 75<=age<=84:
        age75to84=randrange(1,15)
        if age75to84==1:
            print("W",year_of_rule,"roku Twoich rzadow umierasz nagle.")
            if summary_of_rule_points_death>3:
                print("Mieszkancy kolonii szczerze Cie oplakuja, stawiaja Ci swiatynie,liczne pomniki i przekazuja pamiec o Tobie z pokolenia na pokolenie.")
            elif summary_of_rule_points_death==2:    
                print("Mieszkancy kolonii szczerze Cie oplakuja.")
            elif summary_of_rule_points_death==1:
                print("Mieszkancy kolonii oddychaja z ulga.")
            elif summary_of_rule_points_death==0:
                print("Mieszkancy kolonii skladaja dziekczyne ofiary bogom, niszcza Twoj grobowiec a zwloki wyrzucaja do rzeki.")
            alive=False
            quit()
    if age>85:
        age85up=randrange(1,6)
        if age85up==1:
            print("W",year_of_rule,"roku Twoich rzadow umierasz nagle.")
            if summary_of_rule_points_death>3:
                print("Mieszkancy kolonii szczerze Cie oplakuja, stawiaja Ci swiatynie,liczne pomniki i przekazuja pamiec o Tobie z pokolenia na pokolenie.")
            elif summary_of_rule_points_death==2:    
                print("Mieszkancy kolonii szczerze Cie oplakuja.")
            elif summary_of_rule_points_death==1:
                print("Mieszkancy kolonii oddychaja z ulga.")
            elif summary_of_rule_points_death==0:
                print("Mieszkancy kolonii skladaja dziekczyne ofiary bogom, niszcza Twoj grobowiec a zwloki wyrzucaja do rzeki.")
            alive=False
            quit()
    
    
    
        print("-------------------")
        print("-------------------")
        
    
    
    continue