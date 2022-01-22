"""
COMP.CS.100 1.6.4 Index raises
Creator: Tri Phung
Student ID: tuni.fi:K441912
"""

def main():
    nl = '\n'
    benefit = input('Enter the amount of the study benefits: ')
    benefit = float(benefit)
    
    def benefit_raise(amount):
        return (1.17/100 + 1) * amount
    
    benefit_raised = benefit_raise(benefit)
    return_text = f'If the index raise is 1.17 percent, the study benefit,{nl}after a raise, would be {benefit_raised} euros'
    
    print(return_text)
    
    return_text = f'and if there was another index raise, the study{nl}benefits would be as much as {benefit_raise(benefit_raised)} euros'
    
    print(return_text)
    
if __name__ == "__main__":
    main()

