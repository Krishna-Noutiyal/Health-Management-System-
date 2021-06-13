"""
Making a Health Management system which generates exercise and diet plan for 
Krishna, Sagar, Chirag

and Shows the current plan
"""

def getdate():
    import datetime
    return datetime.datetime.now()

time = getdate()



name1 = "Krishna"
name2 = "Sagar"
name3 = "Chirag"
print("\n\n\tHello welcome to Health Management system \n\t\tCreated by - Krishna")

#Name of persons 
def person():
    print("\n\n\tThis program creates or retrives exercise and diet plan for \n")

    print("\t\t1 ->", name1, "\n\t\t2 ->", name2, "\n\t\t3 ->", name3,"\n")

#underline for beauty of program
def line():
    a = print("_"*150,end="\n\n")
    return a

#calling person() function
person()
try:
    #Line for some comfert
    line()

# Create or retrive file
    create_ret = bool(int(input("\n\tWhat you want to do\n\n\t0 -> Create \n\t1 -> Retrive \n\n Note: anyting other than 0 will be considerd as 1\n\n Press 0 or 1 respectively: ")))


    #Line for some comfert
    line()


#asking for diet or exercise
    exe_diet = bool(int(input("\n\n\tWhich file u want to create or retrive\n\n\t0 -> Exercise file \n\t1 -> Diet file\n\n Note: anyting other than 0 will be considerd as 1\n\n Press 0 or 1 respectively: ")))



    #Line for some comfert
    line()


# Name selection

    if create_ret == False and exe_diet == False:
        person()
        name_inp = int(input("\nSelect the person you want to create exercise plan for by pressing 1, 2, or 3 respectively: "))

    elif create_ret == False and exe_diet == True:
        person()
        name_inp = int(input("\nSelect the person you want to create diet plan for by pressing 1, 2, or 3 respectively: "))
    
    elif create_ret == True and exe_diet == False:
        person()
        name_inp = int(input("\nSelect the person you want to retrive exercise plan for by pressing 1, 2, or 3 respectively: "))
    
    elif create_ret == True and exe_diet == True:
        person()
        name_inp = int(input("\nSelect the person you want to retrive diet plan for by pressing 1, 2, or 3 respectively: "))
    

    """
    Creating files Starts
    """

# Diet plan for Krishna
    def diet1():
        """This is diet plan of Krishna"""        
        f = open("Krishna Diet.txt", "w+")
        # Data written in file 
        data = [
                "Hello and welcome to Krishna Diet.txt\n\n",
                "This is the diet plan of Krishna\n\n\n",

                "\t\tIn Morning :-\n\t\tPoha ke sath dahi\n\n\n",

                "\t\tIn Noon :-\n\t\tRoti ke sath Dal or Roti ke sath Sabji\n\n\n",

                "\t\tIn Night :-\n\t\tAnyting light weight and easy to digest\n",

                "\t\t(Note: Eat less at night)\n\n\n",

                "\t\tSnacks:-\n\t\tYou can eat little snacks after noon\n\n\n",

                ]
        
        write = f.writelines(data)
        r = f.readlines()

        f.close()

# Diet plan for Sagar
    def diet2():
        """This is diet plan of Sagar"""        
        f = open("Sagar Diet.txt", "w+")
        # Data written in file 

        data = [
                "Hello and welcome to Sagar Diet.txt\n\n",
                "This is the diet plan of Sagar\n\n\n",

                "\tYou should eat heavy stuff full of fat to grow ur body\n\n\n",

                "\t\tIn Morning :-\n\t\tAllo ka paratha ke sath dahi\n\n\n",

                "\t\tIn Noon :-\n\t\tGhee wali Roti aur Chawal ke sath Dal\n\n\n",

                "\t\tIn Night :-\n\t\tAnyting light weight and easy to digest\n",

                "\t\t(Note: Eat less at night)\n\n\n",
                
                "\t\tSnacks:-\n\t\tYou can eat as much snacks as u want\n\n\n",

                ]
        
        write = f.writelines(data)

        f.close()

# Diet plan for Chirag
    def diet3():
        """This is exercise plan of Chirag"""        
        f = open("Chirag Diet.txt", "w+")
        # Data written in file 
        data = [
                "Hello and welcome to Chirag Diet.txt\n\n",
                "This is the diet plan of Chirag\n\n\n",

                "\tYou should eat less and exercise more\n\n\n",

                "\t\tIn Morning :-\n\t\tRoti ke sath dahi\n\n\n",

                "\t\tIn Noon :-\n\t\tRoti ke sath Dal or Roti ke sath Sabji\n\n\n",

                "\t\tIn Night :-\n\t\tAnyting light weight and easy to digest\n",

                "\t\t(Note: Eat less at night)\n\n\n",

                "\t\tSnacks:-\n\t\tYou should eat as less snacks as u can\n\n\n",

                ]
        write = f.writelines(data)
        r = f.readlines()
                
        f.close()



# Exercise plan for Krishna
    def exe1():
        """This is the exercise plan of Krishna"""        
        f = open("Krishna Exercise.txt", "w+")

        # Data written in file 
        data = [
                "\n\nHello and welcome to Krishna Exercise.txt",
                "\n\nThis is the Exercise plan of Krishna",

                "\n\n\n\tYou have enough stamina but your belly fat and weight is very high\n\tTry out these exercise",


                "\n\n\n\t\tRunning :-\n\t\t\tRunning is a complete workout for body it helps to build your stamina and strengthen your muscles",

            "\n\n\n\tAfter running Exercises",

            # Exercise 1
            "\n\n\n\t\tBurpees :-",

            "\n\n\t\t\tFeature:- This exercise works your core, as well as your chest, shoulders, lats, triceps and quads.\n\t\t\tSince burpees involve explosive plyometric movement, they'll get your heart pumping too.",

            "\n\n\t\tHow to do burpees:- ",

            "\n\n\t\t\tStand with your feet shoulder-distance apart and send your hips back as you lower your body toward the ground in a low squat.\n\t\t\tThen, place your hands right outside of your feet and hop your feet back, allowing your chest to touch the floor.\n\t\t\tPush your hands against the floor to lift your body up into a plank and then jump your feet just outside of your hands.\n\t\t\tWith your weight in your heels, jump explosively into the air with your arms overhead.",

            # Exercise 2
            "\n\n\n\t\tMountain Climbers :-",

            "\n\n\t\t\tFeature:- Mountain Climbers is a moving plank exercise because it worksyour core, in addition to a slew of other body muscles.",

            "\n\n\t\tHow to do mountain climbers:- ",

            "\n\n\t\t\tGet into a high-plank position with your wrists directly under your shoulders.\n\t\t\tKeep your core tight, drawing your belly button in toward your spine.\n\t\t\tDrive your right knee toward your chest and then bring it back to plank.\n\t\t\tThen, drive your left knee toward your chest and bring it back.\n\t\t\tContinue to alternate sides.",

            # Exercise 3
            "\n\n\n\t\tMedicine Ball Burpees :-",

            "\n\n\t\t\tFeature:- Adding a medicine ball to your burpee to increase the intensity of the exercise and boost your metabolism—all while building a sleek set of six-pack abs.",

            "\n\n\t\tHow to do medicine ball burpees:- ",

            "\n\n\t\t\tTanding with your feet shoulder-distance apart, hold a medicine ball with both hands.\n\t\t\tExtend the ball up overhead, then slam the ball down on the ground as hard as you can, hinging over and sitting your butt back as you slam.\n\t\t\tAs you hinge over, bend your knees. Then, drive your left knee toward your chest and bring it back.\n\t\t\tPlace your hands on the ground outside of your feet and jump back into a high-plank position.\n\t\t\tKeep your body in a straight line. Then, jump your feet back towards the outsides of your hands so that you are squatting.\n\t\t\tPick up the ball and press it overhead, extending your body and standing tall."

                
                ]
        
        write = f.writelines(data)
        r = f.readlines()

        f.close()

# Exercise plan for Sagar
    def exe2():
        """This is the exercise plan of Sagar"""        
        f = open("Sagar Exercise.txt", "w+")

        # Data written in file 
        data = [
                "\n\nHello and welcome to Sagar Exercise.txt",
                "\n\nThis is the Exercise plan of Sagar",

                "\n\n\n\tYou have to eat much and do some simple exercise to warm your body\n\tTry out these exercise",

                "\n\n\n\t\tRunning :-\n\t\t\tRunning is a complete workout for body it helps to build your stamina and strengthen your muscles"

                
                ]
        
        write = f.writelines(data)

        f.close()

# Exercise plan for Chirag
    def exe3():
        """This is exercise plan of Chirag"""        
        f = open("Chirag Exercise.txt", "w+")

        # Data written in file 
        data = [
            "\n\nHello and welcome to Chirag Exercise.txt",
            "\n\nThis is the Exercise plan of Chirag",

            "\n\n\n\tYour weight is high as well as ur body figure is very unbalanced\n\tTryout these exercise",
            "\n\nDon't do excessive exercises, do as much as u can.",


            "\n\n\n\t\tRunning :-\n\t\t\tRunning is a complete workout for body it helps to build your stamina and strengthen your muscles",

            "\n\n\n\tAfter running Exercises",

            # Exercise 1
            "\n\n\n\t\tBurpees :-",

            "\n\n\t\t\tFeature:- This exercise works your core, as well as your chest, shoulders, lats, triceps and quads.\n\t\t\tSince burpees involve explosive plyometric movement, they'll get your heart pumping too.",

            "\n\n\t\tHow to do burpees:- ",

            "\n\n\t\t\tStand with your feet shoulder-distance apart and send your hips back as you lower your body toward the ground in a low squat.\n\t\t\tThen, place your hands right outside of your feet and hop your feet back, allowing your chest to touch the floor.\n\t\t\tPush your hands against the floor to lift your body up into a plank and then jump your feet just outside of your hands.\n\t\t\tWith your weight in your heels, jump explosively into the air with your arms overhead.",

            # Exercise 2
            "\n\n\n\t\tMountain Climbers :-",

            "\n\n\t\t\tFeature:- Mountain Climbers is a moving plank exercise because it worksyour core, in addition to a slew of other body muscles.",

            "\n\n\t\tHow to do mountain climbers:- ",

            "\n\n\t\t\tGet into a high-plank position with your wrists directly under your shoulders.\n\t\t\tKeep your core tight, drawing your belly button in toward your spine.\n\t\t\tDrive your right knee toward your chest and then bring it back to plank.\n\t\t\tThen, drive your left knee toward your chest and bring it back.\n\t\t\tContinue to alternate sides.",

            # Exercise 3
            "\n\n\n\t\tMedicine Ball Burpees :-",

            "\n\n\t\t\tFeature:- Adding a medicine ball to your burpee to increase the intensity of the exercise and boost your metabolism—all while building a sleek set of six-pack abs.",

            "\n\n\t\tHow to do medicine ball burpees:- ",

            "\n\n\t\t\tTanding with your feet shoulder-distance apart, hold a medicine ball with both hands.\n\t\t\tExtend the ball up overhead, then slam the ball down on the ground as hard as you can, hinging over and sitting your butt back as you slam.\n\t\t\tAs you hinge over, bend your knees. Then, drive your left knee toward your chest and bring it back.\n\t\t\tPlace your hands on the ground outside of your feet and jump back into a high-plank position.\n\t\t\tKeep your body in a straight line. Then, jump your feet back towards the outsides of your hands so that you are squatting.\n\t\t\tPick up the ball and press it overhead, extending your body and standing tall."

                
                ]
        
        write = f.writelines(data)
        r = f.readlines()
                
        f.close()

    """
    Creating files Ends
    """

    """
    Reading files Starts
    """

#Reading Diet Plan of Krishna
    def read_diet1():
        read = open("Krishna Diet.txt", "r")
        r = read.readlines()
        for lines in r:
            print(lines)
        read.close()
    
#Reading Diet Plan of Sagar
    def read_diet2():
        read = open("Sagar Diet.txt", "r")
        r = read.readlines()
        for lines in r:
            print(lines)
        read.close()

#Reading Diet Plan of Chirag
    def read_diet2():
        read = open("Chirag Diet.txt", "r")
        r = read.readlines()
        for lines in r:
            print(lines)
        read.close()



#Reading Exercise Plan of Krishna
    def read_exe1():
        read = open("Krishna Exercise.txt", "r")
        r = read.readlines()
        for lines in r:
            print(lines)
        read.close()
    
#Reading Exercise Plan of Sagar
    def read_exe2():
        read = open("Sagar Exercise.txt", "r")
        r = read.readlines()
        for lines in r:
            print(lines)
        read.close()

#Reading Exercise Plan of Chirag
    def read_exe2():
        read = open("Chirag Exercise.txt", "r")
        r = read.readlines()
        for lines in r:
            print(lines)
        read.close()

    """
    Reading files ends
    """

# Function for Printing the diet plans
    def diet():
        # Diet plan of Krishna
        if name_inp == 1:

            print("\n\n\tDiet plan for", name1,"has been created successfully\n\n\t\tHurreeyh!!\n")

            a = diet1()

        # Diet plan of Sagar
        elif name_inp == 2:

            print("\n\n\tDiet plan for", name2,"has been created successfully\n\n\t\tHurreeyh!!\n")

            a = diet2()

        # Diet plan of Chirag
        elif name_inp == 3:
            
            print("\n\n\tDiet plan for", name3,"has been created successfully\n\n\t\tHurreeyh!!\n")

            a = diet3()

        # if value enter by user is other then 1, 2, or 3
        elif name_inp<1 or name_inp>3:

            print("\n\n\tPlease choose the correct option and try again\n")
# Function for Printing the exercise plans
    def exe():
        # Diet plan of Krishna
        if name_inp == 1:

            print("\n\n\tExercise plan for", name1,"has been created successfully\n\n\t\tHurreeyh!!\n")

            a = exe1()

        # Diet plan of Sagar
        elif name_inp == 2:

            print("\n\n\tExercise plan for", name2,"has been created successfully\n\n\t\tHurreeyh!!\n")

            a = exe2()

        # Diet plan of Chirag
        elif name_inp == 3:
            
            print("\n\n\tExercise plan for", name3,"has been created successfully\n\n\t\tHurreeyh!!\n")

            a = exe3()

        # if value enter by user is other then 1, 2, or 3
        elif name_inp<1 or name_inp>3:

            print("\n\n\tPlease choose the correct option and try again\n")

# Function for Printing the diet plans
    def read_diet():
        # Diet plan of Krishna
        if name_inp == 1:

            print("\n\n\tPress enter to print the diet plan of", name1)
            ent = input(": ")
            print("\n\n")
            a = read_diet1()

        # Diet plan of Sagar
        elif name_inp == 2:

            print("\n\n\tPress enter to print the diet plan of", name2)
            ent = input(": ")
            print("\n\n")
            a = read_diet2()

        # Diet plan of Chirag
        elif name_inp == 3:
            
            print("\n\n\tPress enter to print the diet plan of", name3)
            ent = input(": ")
            print("\n\n")
            a = read_diet3()

        # if value enter by user is other then 1, 2, or 3
        elif name_inp<1 or name_inp>3:

            print("\n\n\tPlease choose the correct option and try again\n")
# Function for Printing the exercise plans
    def read_exe():
        # Diet plan of Krishna
        if name_inp == 1:

            print("\n\n\tPress enter to print the exercise plan of", name1)
            ent = input(": ")

            a = read_exe1()

        # Diet plan of Sagar
        elif name_inp == 2:

            print("\n\n\tPress enter to print the exercise plan of", name2)
            ent = input(": ")

            a = read_exe2()

        # Diet plan of Chirag
        elif name_inp == 3:
            
            print("\n\n\tPress enter to print the exercise plan of", name3)
            ent = input(": ")

            a = read_exe3()

        # if value enter by user is other then 1, 2, or 3
        elif name_inp<1 or name_inp>3:

            print("\n\n\tPlease choose the correct option and try again\n")



    # running diet function when file needs to be created 
    if create_ret== False and exe_diet == True:
        diet_plan_func = diet()

    elif create_ret == False and exe_diet == False:
        exe_plan_func = exe()
        
    elif create_ret == True and exe_diet == True:
        print(time,"\n\n")
        read_diet_plan_func = read_diet()

    elif create_ret == True and exe_diet == False:
        print(time,"\n\n")
        read_exe_plan_func = read_exe()
    
    else:
        print("You did someting wrong try again")
except Exception as e:
    # print(e)
    print("\n\n\t\tUnable to retrive the file: File not found\n\n\t\t\tPlease create the file first\n\n")

close = input("\n\nPress enter to close: ")
print()
