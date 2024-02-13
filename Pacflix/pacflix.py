from datetime import datetime
from dateutil.relativedelta import relativedelta

class Pacflix():
    list_of_referral_code = []
    
    def __init__(self, user_name):
        # set ke None karena defaultnya adalah kosong (user blm dibuat)
        self.user_name = user_name
        self.start_date = None
        self.end_date = None
        self.current_plan = None
        self.duration = 0
        
        # push referal code setiap user baru terbuat
        Pacflix.list_of_referral_code.append(self.user_name)
        print(f'Your account successfully created, share this code "{self.user_name}" to your friend to get some benefits!')
    
    def list_plan(self):
        print('List of Pacflix plan: ')
        print('1. Basic Plan')
        print('SD, 1 device, Movie, Rp120.000,-')
        print()
        print('2. Standard Plan')
        print('HD, 2 device, Movie + Sports, Rp160.000,-')
        print()
        print('3. Premium Plan')
        print('UHD, 3 device, Movie + Sports + News, Rp200.000,-')
    
    def check_plan(self):
        if(self.current_plan == None):
            print('You do not have any plan!')
        else:
            print(f'Your current plan is {self.current_plan}')
            print(f'Start subscribe at {self.start_date}')
            print(f'End subscribe at {self.end_date}')
    
    def purchase(self, new_plan, ref_code, duration):
        total_price = 0
        
        # ref code ada (berarti ga kosong) dan ref code valid
        if((ref_code != None) and (ref_code in Pacflix.list_of_referral_code)):
            self.duration = duration
            self.start_date = datetime.now()
            self.end_date = self.start_date + relativedelta(months=duration)
            
            if(new_plan == 'Basic Plan'):
                self.current_plan = 'Basic Plan'
                total_price = (120_000-(0.04 * 120_000))
                print(f'You selected Basic Plan with referral code, the price will be {total_price}')
                
            elif(new_plan == 'Standard Plan'):
                self.current_plan = 'Standard Plan'
                total_price = (160_000-(0.04 * 160_000))
                print(f'You selected Standard Plan with referral code, the price will be {total_price}')
                
            elif(new_plan == 'Premium Plan'):
                self.current_plan = 'Premium Plan'
                total_price = (200_000-(0.04 * 200_000))
                print(f'You selected Premium Plan with referral code, the price will be {total_price}')
                
            else:
                self.duration = 0
                print('Your selected plan is invalid!')
        
        # ref code ada tapi invalid
        elif((ref_code != None) and (ref_code not in Pacflix.list_of_referral_code)):
            print('Your referral code is invalid!')
        
        # ref code tidak ada (tidak dimasukkan)
        elif((ref_code == None)):
            self.duration = duration
            self.start_date = datetime.now()
            self.end_date = self.start_date + relativedelta(months=duration)
            
            if(new_plan == 'Basic Plan'):
                self.current_plan = 'Basic Plan'
                total_price = 120_000
                print(f'You selected Basic Plan with total price {total_price}')
                
            elif(new_plan == 'Standard Plan'):
                self.current_plan = 'Standard Plan'
                total_price = 160_000
                print(f'You selected Standard Plan with total price {total_price}')
                
            elif(new_plan == 'Premium Plan'):
                self.current_plan = 'Premium Plan'
                total_price = 200_000
                print(f'You selected Premium Plan with total price {total_price}')
                
            else:
                self.duration = 0
                print('Your selected plan is invalid!')
        
        else:
            print('Something bad happen....')
    
    def upgrade_plan(self, new_plan):
        subs_time = self.end_date - datetime.now()
        total_price = 0
        
        # subscription time > 12 bulan, dapat diskon
        if(subs_time.days > 360):
            if(self.current_plan == 'Basic Plan'):
                if(new_plan == 'Standard Plan'):
                    self.current_plan = 'Standard Plan'
                    total_price = (160_000 - (160_000 * 0.05))
                    print(f'Upgrade to {self.current_plan}, price {total_price}')
                    
                    
                elif(new_plan == 'Premium Plan'):
                    self.current_plan = 'Premium Plan'
                    total_price = (200_000 - (200_000 * 0.05))
                    print(f'Upgrade to {self.current_plan}, price {total_price}')
                    
                else:
                    print('Your selected new plan is invalid!')
                
            elif(self.current_plan == 'Standard Plan'):
                if(new_plan == 'Premium Plan'):
                    self.current_plan = 'Premium Plan'
                    total_price = (200_000 - (200_000 * 0.05))
                    print(f'Upgrade to {self.current_plan}, price {total_price}')
                
            else:
                print('You are in the highest tier, cannot upgrade subscription!')
        
        # subscription time < 12 bulan, tidak dapat diskon
        else:
            if(self.current_plan == 'Basic Plan'):
                if(new_plan == 'Standard Plan'):
                    self.current_plan = 'Standard Plan'
                    total_price = 160_000
                    print(f'Upgrade to {self.current_plan}, price {total_price}')
                    
                    
                elif(new_plan == 'Premium Plan'):
                    self.current_plan = 'Premium Plan'
                    total_price = 200_000
                    print(f'Upgrade to {self.current_plan}, price {total_price}')
                    
                else:
                    print('Your selected new plan is invalid!')
                
            elif(self.current_plan == 'Standard Plan'):
                if(new_plan == 'Premium Plan'):
                    self.current_plan = 'Premium Plan'
                    total_price = 200_000
                    print(f'Upgrade to {self.current_plan}, price {total_price}')
                
            else:
                print('You are in the highest tier, cannot upgrade subscription!')