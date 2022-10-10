import os

from form_and_check import check
from form_and_check import fmt

class ROI():
    def __init__(self):
        self.tot_inc = 0.0
        self.tot_exp = 0.0
        self.tot_cf = 0.0
        self.coc_roi = 0.0
        self.rental_inc = 0.0
        self.washer = 0.0
        self.dryer = 0.0
        self.laundry = 0.0
        self.storage = 0.0
        self.other = 0.0
        self.mortgage = 0.0
        self.prop_tax = 0.0
        self.insurance = 0.0
        self.electric = 0.0
        self.water = 0.0
        self.sewer = 0.0
        self.garbage = 0.0
        self.gas = 0.0
        self.internet = 0.0
        self.hoa = 0.0
        self.lawn = 0.0
        self.vacancy = 0.0
        self.repairs = 0.0
        self.capEx = 0.0
        self.management = 0.0
        self.down_payment = 0.0
        self.closting_costs = 0.0
        self.rehab_budget = 0.0
        self.misc_other = 0.0
        self.inv_tot = 0.0
        self.annual_cash_flow = 0.0
        self.address = ''
        self.prop_dict = {                  # dictionary for output or database storage
            'address':self.address,
            'tot_inc':self.tot_inc, 
            'tot_exp':self.tot_exp, 
            'tot_cf':self.tot_cf, 
            'coc_roi':self.coc_roi, 
            'rental_inc':self.rental_inc, 
            'washer':self.washer, 
            'dryer':self.dryer, 
            'laundry':self.laundry, 
            'storage':self.storage, 
            'other':self.other, 
            'mortgage':self.mortgage, 
            'prop_tax':self.prop_tax, 
            'insurance':self.insurance, 
            'electric':self.electric, 
            'water':self.water, 
            'sewer':self.sewer, 
            'garbage':self.garbage, 
            'gas':self.gas, 
            'internet':self.internet, 
            'hoa':self.hoa, 
            'lawn':self.lawn, 
            'vacancy':self.vacancy, 
            'repairs':self.repairs, 
            'capEx':self.capEx, 
            'management':self.management, 
            'down_payment':self.down_payment, 
            'closting_costs':self.closting_costs, 
            'rehab_budget':self.rehab_budget, 
            'misc_other':self.misc_other, 
            'inv_tot':self.inv_tot, 
            'annual_cash_flow':self.annual_cash_flow
        }
    
    def get_address(self):                  # gets address for future dictionary retrieval
        self.address = input('What is the address of the property?  ')
        return self.address

    def output(self):                       # aligns the text for output
        os.system('cls')
        print(f'\n{self.address:^112}\n')
        print('\t\t\t\t\t\t\t|')
        text1 = 'Income'
        text2 = 'Cash Flow'
        print(f'{text1:^56}|{text2:^56}')
        print('\t\t\t\t\t\t\t|')
        print(f'\tRental Income:\t\t{(fmt(self.rental_inc)).rjust(15)}\t\t|')
        print(f'\tWashing Machine:\t{(fmt(self.washer)).rjust(15)}\t\t|')
        print(f'\tDryer:\t\t\t{(fmt(self.dryer)).rjust(15)}\t\t|')
        print(f'\tLaundry Room:\t\t{(fmt(self.laundry)).rjust(15)}\t\t|')
        print(f'\tStorage Unit:\t\t{(fmt(self.storage)).rjust(15)}\t\t|\tTotal Monthly Income:\t{(fmt(self.tot_inc)).rjust(15)}')
        print(f'\tOther:\t\t\t{(fmt(self.other)).rjust(15)}\t\t|\tTotal Monthly Expenses:\t{(fmt(self.tot_exp)).rjust(15)}')
        print('\t\t\t\t\t\t\t|')
        print(f'\tTotal Monthly Income:\t{(fmt(self.tot_inc)).rjust(15)}\t\t|\tTotal Monthly Expenses:\t{(fmt(self.tot_cf)).rjust(15)}')
        print('\t\t\t\t\t\t\t|')
        print('---------------------------------------------------------------------------------------------------------------')
        print('\t\t\t\t\t\t\t|')
        text3 = 'Expenses'
        text4 = 'Cash on Cash ROI'
        print(f'{text3:^56}|{text4:^56}')
        print('\t\t\t\t\t\t\t|')
        print(f'\tMortgage:\t\t{(fmt(self.mortgage)).rjust(15)}\t\t|')
        print(f'\tProperty Tax:\t\t{(fmt(self.prop_tax)).rjust(15)}\t\t|')
        print(f'\tInsurance:\t\t{(fmt(self.insurance)).rjust(15)}\t\t|')
        print(f'\tElectric:\t\t{(fmt(self.electric)).rjust(15)}\t\t|')
        print(f'\tWater:\t\t\t{(fmt(self.water)).rjust(15)}\t\t|')
        print(f'\tSewer:\t\t\t{(fmt(self.sewer)).rjust(15)}\t\t|')
        print(f'\tGarbage:\t\t{(fmt(self.garbage)).rjust(15)}\t\t|\tDown Payment:\t\t{(fmt(self.down_payment)).rjust(15)}')
        print(f'\tGas:\t\t\t{(fmt(self.gas)).rjust(15)}\t\t|\tClosing Costs:\t\t{(fmt(self.closting_costs)).rjust(15)}')
        print(f'\tInternet:\t\t{(fmt(self.internet)).rjust(15)}\t\t|\tRehab Budget:\t\t{(fmt(self.rehab_budget)).rjust(15)}')
        print(f'\tHoa:\t\t\t{(fmt(self.hoa)).rjust(15)}\t\t|\tMisc Other:\t\t{(fmt(self.misc_other)).rjust(15)}')
        print(f'\tLawn:\t\t\t{(fmt(self.lawn)).rjust(15)}\t\t|')
        print(f'\tVacancy:\t\t{(fmt(self.vacancy)).rjust(15)}\t\t|\tTotal Investment:\t{(fmt(self.inv_tot)).rjust(15)}')
        print(f'\tRepairs:\t\t{(fmt(self.repairs)).rjust(15)}\t\t|')
        print(f'\tCapex:\t\t\t{(fmt(self.capEx)).rjust(15)}\t\t|\tMonthly Cash Flow:\t{(fmt(self.tot_cf)).rjust(15)}')
        print(f'\tManagement:\t\t{(fmt(self.management)).rjust(15)}\t\t|\tAnnual Cash Flow:\t{(fmt(self.annual_cash_flow)).rjust(15)}')
        print('\t\t\t\t\t\t\t|')
        print(f'\tTotal Monthly Expenses:\t{(fmt(self.tot_exp)).rjust(15)}\t\t|\tCash on Cash ROI:\t{(fmt(self.coc_roi)).rjust(15)}')        
        print('\t\t\t\t\t\t\t|')      
        print('')

    def income(self):                   # income data is gathered through input and
        calc.output()                   # displayed every time new data is entered
        self.rental_inc = check(input('What is your rental income per month?  '))
        calc.output()
        self.washer = check(input('What is your washing machine income per month?  '))
        calc.output()
        self.dryer = check(input('What is your dryer income per month?  '))
        calc.output()
        self.laundry = check(input('What is your laundry room income per month?  '))
        calc.output()
        self.storage = check(input('What is your storage income per month?  '))
        calc.output()
        self.other = check(input('Do you have any other income you would like to add on a per month basis?  '))
        self.tot_inc = self.rental_inc + self.washer + self.dryer + self.laundry + self.storage + self.other
        calc.output()
        print(f'Your total income is ${fmt(self.tot_inc)} per month.\n')

    def expense(self):                  # income data is gathered through input and
        self.mortgage = check(input('What will be your mortgage payment on a per month basis?  '))
        calc.output()                   # displayed every time new data is entered
        self.prop_tax = check(input('What will be your property taxes on a per month basis?  '))
        calc.output()
        self.insurance = check(input('How much will your insurance be on a per month basis?  '))
        calc.output()
        self.electric = check(input('Please estimate how much electricity will cost you every month.  '))
        calc.output()
        self.water = check(input('Please estimate how much water will cost you every month.  '))
        calc.output()
        self.sewer = check(input('Please estimate how much sewer will cost you every month.  '))
        calc.output()
        self.garbage = check(input('Please estimate how much garbage collection will cost you every month.  '))
        calc.output()
        self.gas = check(input('Please estimate how much natural gas will cost you every month.  '))
        calc.output()
        self.internet = check(input('Please estimate how much internet will cost you every month.  '))
        calc.output()
        self.hoa = check(input('Please estimate how much the HOA fees will cost you every month.  '))
        calc.output()
        self.lawn = check(input('Please estimate how much lawn and garden care will cost you every month.  '))
        calc.output()
        self.vacancy = check(input('How much would like to put away every month to account for vacancy of the unit?  '))
        calc.output()
        self.repairs = check(input('Please estimate how much repairs and maintenance will cost you every month.  '))
        calc.output()
        self.capEx = check(input('Please estimate how much your capital expenditures will be every month.  '))
        calc.output()
        self.management = check(input('Please estimate how much property management will cost you every month.  '))
        self.tot_exp = self.mortgage + self.prop_tax + self.insurance + self.electric + self.water + self.sewer + self.garbage + self.gas + self.internet + self.hoa + self.lawn + self.vacancy + self.repairs + self.capEx + self.management
        calc.output()
        print(f'Your total expenses are {fmt(self.tot_exp)} per month.\n')

    def cash_flow(self):                # calculation and printing of cash flow
        self.tot_cf = self.tot_inc - self.tot_exp
        if self.tot_cf == 0:           # check to make sure that expenses are not zero (0)
            div_0 = input('The total for all expenses cannot be Zero (0). Please hit any key to start over or type "q" to quit.')
            if div_0 == 'q':            # if expenses were zero (0), we would get a ZeroDivisionError
                exit()
            else:
                bp_roi_tool()
        calc.output()                   # displayed every time new data is entered
        print(f'Your total expenses are {fmt(self.tot_exp)} per month.\n')
        print(f'Your total cashflow is {fmt(self.tot_cf)} per month.\n')

    def roi(self):                      # calculation of ROI, annual cash flow
        self.annual_cash_flow = self.tot_cf * 12
        self.down_payment = check(input('How much will you be putting down for the down payment?  '))
        calc.output()
        self.closting_costs = check(input('Please estimate how much your closing costs will be.  '))
        calc.output()
        self.rehab_budget = check(input('What is your budget for rehab on this project?  '))
        calc.output()
        self.misc_other = check(input('Are there any other funds you would like to add to this calculation?  '))
        self.inv_tot = self.down_payment + self.closting_costs + self.rehab_budget + self.misc_other
        self.coc_roi = (self.annual_cash_flow / self.inv_tot) * 100
        calc.output()
        print(f'Your total cash invested is {fmt(self.inv_tot)}.')
        print(f'Your cashflow is {fmt(self.annual_cash_flow)} annually.')
        print(f'Your Cash on Cash Return on Investment (ROI) is {fmt(self.coc_roi)}% annually.\n')
        print('Your data will be kept on our servers.\nFuture versions of this program will allow you to reprocess ROI\nusing this data on this property to start with.')
        print('If you do not want your data stored on our servers, you may keep\nthe data by storing text that can be entered in at a future date.')
        print_dict = input('Would you like the data stored on our servers? "y" or "n"  ')
        if print_dict == 'y':
            print('Your data will be stored in a database on our servers. Thank you for using\nthe McCarthy Cash on Cash ROI calculator. Have a nice day!!!')
            return self.prop_dict
        if print_dict == 'n':
            print('No worries. Just store the following information as is, and in the future,\nyou will be able to enter it into our program to work with again.\nThank you and have a nice day!!!')
            print(self.prop_dict)
    
    def exit_func():
        exit()

# --------------------------------- Main Body --------------------------------- #

calc = ROI()
def bp_roi_tool():
    os.system('cls')
    print('Welcome to the McCarthy Cash on Cash ROI calculator.')
    start = input('Would you like to calculate the Cash on Cash ROI for an investment property?  "y" or "n"  ')
    if start == 'n':
        exit()
    elif start == 'y':
        calc.get_address()
        calc.output()
        calc.income()
        calc.expense()
        calc.cash_flow()
        calc.roi()
    else:
        print('Please type "y" or "n".')
        bp_roi_tool()

bp_roi_tool()