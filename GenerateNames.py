import pandas as pd
import numpy as np
import random

class GenerateData:
    def __init__(self, names_path, name_length=3, M_F_ration=0.5):
        """Read Full names with specific length

        Parameters:
        names_path (str): the path to names file and should be csv file.

        name_length (int): the number of names in the generated full name default 3.

        M_F_ration (float): the ration between[0,1] of the female names to male names default 0.5, heighr of the number more Female names.
        """
        # assert names_path == None or names_path == "", "Enter the path to name file and should be .csv"
        self.name_length = name_length
        self.M_F_ration = M_F_ration
        self.M_F_ration = M_F_ration
        self.names = pd.read_csv(names_path)

    def Generate_Normal(self, number_of_names, saveto=""):
        """Generate normal names

        Parameters:
        number_of_names (int): the number of generated names.
        saveto (str): the location to save the generated names as csv if not entred csv file will not be saved.
        """
        Gnames = []
        for j in range(number_of_names):
            # radnom sample to select the next the name will be male or female
            if np.random.sample() > self.M_F_ration:
                random_name = self.names[self.names.Gender=="M"].sample(n=self.name_length).Name.values
                Gnames.append([" ".join(random_name), "M"])
            else:
                random_name = self.names[self.names.Gender=="F"].sample(n=1).Name.values
                random_name = np.append(random_name, self.names[self.names.Gender=="M"].sample(n=self.name_length - 1).Name.values) 
                Gnames.append([" ".join(random_name), "F"])

        Gnames = pd.DataFrame(Gnames, columns=["Name", "Gender"])  
        if saveto !="":
            Gnames = Gnames.to_csv(saveto, index=False)
        return Gnames
    


    def _Add_noise(self, name, unique_charachter, min_noise, max_noise):
        char_toadd = np.random.choice(range(min_noise, max_noise))
        for char in range(char_toadd):
            index_to_add = np.random.choice(range(0,len(name)))
            char_to_add = np.random.choice(unique_charachter)
            name = name[:index_to_add] + char_to_add +  name[index_to_add:]
        return name
            

    def _shuffel_name(self, name):
        done =True
        fname = name.split()[0]
        while done:
            splited_name = name.split()
            random.shuffle(splited_name)
            name = " ".join(splited_name)
            if fname != name.split()[0]:
                done =False
        return name
    


    def Generate_Fake_Names(self, number_of_names, saveto="", min_noise=1, max_noise=10, shuffel_F=0.1 ):
        unique_charachter = list(set("".join(self.names.Name.values).replace(" ", "")))

        Gnames = []
        for j in range(number_of_names):
            # radnom sample to select the next the name will be male or female
            if np.random.sample() > self.M_F_ration:
                random_name = self.names[self.names.Gender=="M"].sample(n=self.name_length).Name.values
                fakeName = self._Add_noise(" ".join(random_name), unique_charachter, min_noise, max_noise)
                Gnames.append([fakeName, "M"])
            else:
                random_name = self.names[self.names.Gender=="F"].sample(n=1).Name.values
                random_name = np.append(random_name, self.names[self.names.Gender=="M"].sample(n=self.name_length - 1).Name.values) 
                fakeName = self._Add_noise(" ".join(random_name), unique_charachter, min_noise, max_noise)

                if np.random.sample() < shuffel_F:
                    fakeName = self._shuffel_name(fakeName)

                Gnames.append([fakeName, "F"])

        Gnames = pd.DataFrame(Gnames, columns=["Name", "Gender"])  
        if saveto !="":
            Gnames = Gnames.to_csv(saveto, index=False)
        return Gnames
