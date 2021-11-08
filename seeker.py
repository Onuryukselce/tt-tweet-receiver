import twint
from datetime import date, timedelta, datetime

class Seeker:

    def get_tweets_from_user_with_replies_by_date(self,user,start_date, end_date = 0):
        """ self.__get_timeline_of_user(user)
        self.__get_all_replies(user)"""
        if(end_date == 0):
            end_date = datetime.now("%d/%m/%Y")
        self.__get_tweets_by_date(user,start_date, end_date)
        self.__get_replies_by_date(user,start_date, end_date)

    def get_all_timeline_of_user(self, user):
        self.__get_timeline_of_user(user)
        self.__get_all_replies(user)




    def __get_timeline_of_user(self,user):
        timelineConfig = twint.Config()
        timelineConfig.Username = user
        timelineConfig.Profile_full = True
        timelineConfig.Output = "timeline_data_of_"+user+".csv"
        timelineConfig.Store_csv =True
        twint.run.Profile(timelineConfig)

    def __get_tweets_by_date(self,user,start_date,end_date):
        tweetsByDate = twint.Config()
        tweetsByDate.Username = user
        tweetsByDate.Store_csv = True
        start_date = datetime.strptime(start_date, "%d/%m/%Y")
        end_date = datetime.strptime(end_date, "%d/%m/%Y")
        for single_date in self.__daterange(start_date, end_date):
            tmp_start_date = single_date.strftime("%Y-%m-%d")
            tmp_end_date = (single_date + timedelta(days=1)).strftime("%Y-%m-%d")
        
            print("sd = " + tmp_start_date)
            print("ed= " + tmp_end_date)
            tweetsByDate.Output = user+"_"+tmp_start_date+"_"+tmp_end_date+".csv"

            tweetsByDate.Since = tmp_start_date
            tweetsByDate.Until = tmp_end_date
            try:
                twint.run.Search(tweetsByDate)
            except:
                twint.run.Search(tweetsByDate)
        

    def __get_replies_by_date(self,user,start_date,end_date):
        repliesByDate = twint.Config()
        repliesByDate.To = user
        repliesByDate.Store_csv =True
        start_date = datetime.strptime(start_date, "%d/%m/%Y")
        end_date = datetime.strptime(end_date, "%d/%m/%Y")
        for single_date in self.__daterange(start_date, end_date):
            tmp_start_date = single_date.strftime("%Y-%m-%d")
            tmp_end_date = (single_date + timedelta(days=1)).strftime("%Y-%m-%d")
            print("sd = " + tmp_start_date)
            print("ed= " + tmp_end_date)
            repliesByDate.Output = "replies_to_"+user+"_"+tmp_start_date+"_"+tmp_end_date+".csv"

            repliesByDate.Since = tmp_start_date
            repliesByDate.Until = tmp_end_date
            try:
                twint.run.Search(repliesByDate)
            except:
                twint.run.Search(repliesByDate)
        

    def __get_all_replies(self,user):
        replies = twint.Config()
        replies.To = user
        replies.Output = "all_replies_to_"+user+".csv"
        replies.Store_csv =True
        twint.run.Search(replies)

    def __daterange(self,start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)


    pass