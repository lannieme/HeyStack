import numpy as np
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
#nltk.download()

class HeyStack (object):
    def __init__(self):
        pass

    def preprocessing(self, input_sent):
        if input_sent == "Hey Stack!":
            ans = "Hi Alexis! How may I help you today?"
            files = None

            self.json_generate(ans, files)

        else:

            #input = nltk.word_tokenize(input_sent)
            #print input
            input_sent = input_sent.strip("?")
            word_list = [WordNetLemmatizer().lemmatize(word, "v") for word in input_sent.split(" ")]
            #print word_list

            #TODO: only number
            time_frame = self.get_time(word_list)
            orderby_claus = self.get_orderby(word_list)

            word_tag = nltk.pos_tag(word_list)
            #print word_tag
            attribute_list = []
            for x in word_tag:
                if x[1] == "NN":
                    attribute_list.append(x[0])
            #print attribute_list

            select_claus = self.get_select(attribute_list)
            from_claus = self.get_from(attribute_list)
            where_claus = self.get_where(attribute_list)
            groupby_claus = self.get_groupby(attribute_list)

            print (select_claus, time_frame, from_claus, where_claus, groupby_claus, orderby_claus)

            self.translation(select_claus, time_frame, from_claus, where_claus, groupby_claus, orderby_claus)

    def translation(self, select_claus, time_frame, from_claus, where_claus, groupby_claus, orderby_claus):
        pass


    def json_generate(self, convID = None, qustionID = None, ans=None, files=None):
        response = {
            "convID": None,
            "questionID": None,
            "ans": ans,
            "files": files
        }

        return response

    def get_time(self, input):
        today = [3, 22, 2018]
        time_line = ["day", "month", "quarter", "year"]

        result = []
        for cur_time in time_line:
            if cur_time in input:
                time = cur_time
        if "last" in input:
            if time == "month":
                month = today[0] - 1
                year = today[2]
                if month == 0:
                    month == 12
                    year = year - 1
                if month == 2:
                    days = 28
                else:
                    days = 31
                for cur_day in range(days):
                    if cur_day < 10:
                        cur_day = "0" + str(cur_day)
                    result.append(str(month)+"/"+str(cur_day)+"/"+str(year))

        #TODO: case when he wants month in last year

        return result

    def get_select(self, input):
        attribute_list = ["city", "state", "country", "profit", "revenue"]

        result = []
        for cur_attribute in attribute_list:
            if cur_attribute in input:
                result.append(cur_attribute)
        if "revenue" in result:
            result[result.index("revenue")] = "SUM(Purchase_Amount)"
            print "yes"

        return result

    def get_from(self, input):

        return []

    def get_where(self, input):

        return ["date"]

    def get_groupby(self, input):

        return ["state"]

    def get_orderby(self, input):
        order_list = ["average", "minimum", "most"]

        result = []
        for cur_attribute in order_list:
            if cur_attribute in input:
                order = cur_attribute

        if order == "most":
            result.append("DESC")

        return result


my_class = HeyStack()
my_class.preprocessing("In which state did we generate the most revenue last month?")
#SELECT "State_ID, Sum(Purchse_Amount)" as A FROM Purchases WHERE Purchse_Date "BETWEEN 02/01/2017 AND 02/28/2017" GROUP BY "State_ID" ORDER BY A "DESC"
