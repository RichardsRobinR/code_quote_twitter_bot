import json
 
class GenerateNewQuote :
          
    def generateNew(self):    
    # Opening JSON file
        self.quotes_data_file = open('quotes_data.json')
        
        # returns JSON object as a dictionary
        self.quotes_data = json.load(self.quotes_data_file)

        with open('sample.json','r+') as file:
                # First we load existing data into a dict.
                file_data = json.load(file)

                self.quote_dictionary = self.quotes_data['quotes'][len(file_data["completed_quotes"])]
            
                # Join new_data with file_data inside emp_details
                file_data["completed_quotes"].append(self.quote_dictionary)
                # Sets file's current position at offset.
                file.seek(0)
                # convert back to json.
                json.dump(file_data, file, indent = 4)

                file.close()

        # print(len(data['quotes']))
        # print(data['quotes'][len(file_data["completed_quotes"])])
        
        self.quotes_data_file.close()

        return self.quote_dictionary
    

# generateNewQuote = GenerateNewQuote()
# print(generateNewQuote.generateNew())
