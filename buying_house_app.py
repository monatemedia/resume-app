import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Sentinel Financial
##### *Buying Your First Home* 
''')

image = Image.open('sentinel-logo.png')
st.image(image, width=150)

st.markdown('## Some Housekeeping First', unsafe_allow_html=True)
st.info('''
- This is not financial advice. This is just an account of my own personal experience, my thoughts on what to be on the lookout for and a calculator to help you figure out how much real estate actually costs. 
- This app is written from the South African perspective, but it is written for a global audience. Therefore, many of the points I raise here will be applicable in your jurisdiction.
- The calculator included is based on commonly accepted financial principles.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.monatemedia.com" target="_blank">Monate Media</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Authentication</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Investments</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Last Will</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Life Assurance</a>
      </li>      
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Markets</a>
      </li>
            <li class="nav-item">
        <a class="nav-link" href="#social-media">Mortgages</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Switch to Commercial</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## How I Bought My First Apartment
''')

st.markdown('When I bought my apartment, the real estate agent sent the offer-to-purchase to a bond originator to go to the banks and get me a bond loan for the property. All the banks declined.')
st.markdown('Naturally I thought it was my bad credit, and the fact that I worked on `100%` commission. I called the originator anyway to find out what happened. Well, turns out that the originator had contracts with only three of the four big banks, and the banks all declined due to reasons related to how they manage their balance sheet. It was never about me anyway.')
st.markdown('I called the agent and told her contractually, in terms of the offer-to-purchase, I still had time to get a bond and that she cannot send the property back to market. I took the contract to the fourth big bank and did the bond application myself. This app was successful and I was given the bond. Great!')
st.markdown('Anyways, the current owner had to pay for an electrical and plumbing certificate that certified that the property is in good condition. This is a normal process when buying a place because the bank doesn’t want to give you money for a place that is uninhabitable.')
st.markdown('A few weeks later I get a call from the bank’s conveyancing attorneys for an appointment for me to come sign the bond registration papers. They had me sign a stack of documents. Did read it? Of course not. Nobody reads the contract anyways, right?')

#####################
st.markdown('''
## How Property Purchase Transactions Happen
''')

st.markdown('One of the main things that happens in this whole property purchase transaction is that the new home owner only actually sees the monthly bond instalment when they are sitting across from the attorneys, at which point you’d feel sheepish to say to the attorney that you want to read it first. These guys also know how to put pressure on you to pen the contract, because they are usually in such a “hurry” that you can come away feeling like you’re wasting their time.')
st.markdown('Before you go see the attorneys, tell them to email you the contract ahead of time so that you can review it and have your questions ready for the in-person meeting. Don’t let anybody rush you through signing off on a 20-year commitment. Once it’s done, it’s difficult to undo.')
st.markdown('You are the customer, and these professionals charge a lot of money for this one transaction. Get your money’s worth, but respect the people’s time.')

#####################
st.markdown('''
## Key Questions To Ask
''')
st.markdown('Some key questions to ask the current owner when viewing the property:')
st.markdown('- Is electricity and water prepaid or does the bill come end of the month?')
st.markdown('- How much are they currently paying for water/electricity?')
st.markdown('- In a complex, how much are the levies and management agent charging monthly?')
st.markdown('- How much are the rates with the municipality? Rates are basically a land tax charged to people who own property.')
st.markdown('- If you are going to be renting out the property, ask the owner how much these properties rent for in the current market so you have an indication.')
st.markdown('- What, in the owner’s opinion, are the most urgent repairs that need to take place pretty soon.')
st.markdown('- Ask some general questions about the neighbours and the neighbourhood.')
st.markdown('There a no dumb questions when making this kind of commitment. Make sure you write down your questions and that you populate the answers on your sheets. It’s easy to forget the detail.')
st.markdown('- `Bonus tip:` If you are buying especially an older free-standing house, tell the agent when signing the offer to purchase that you will hire your own roof specialist, builder, electrician, plumber and pool guy to do an independent report. These people cost you money, of course, but their loyalty belongs to you and not to the seller and his estate agent.')
st.markdown('It is cheaper to burn some money at the outset and turn down the deal than it is to discover a nasty cracked wall or a leaking roof that compromises the entire structure. You use this information to negotiate a further discount on the property or you ask the current owner to fix these things as part of the transaction before you take ownership. Make sure what is agreed to it committed to black on white.')
st.markdown('Now the bank usually will require collateral from you for in the unlikely event that you kick the bucket. Sometimes they will provide it to you in the form of bond cover, other times they will request you to purchase a life cover policy which you will cede to the bank. Life cover can be purchased from an insurance company.')
st.markdown('You see, banks are in the money lending game… they’re not in the property game. They want to know if you pass away, they are going to get their money back. That way your family gets to keep the house too.')
st.markdown('Then there are the conveyancing fees and transfer tax/duty. Conveyancing fees are fees paid to property attorneys to affect the transfer with the deed’s office on your behalf and the transfer duty is a tax on the purchase of the property. These are once off fees.')
st.markdown('Sometimes, if you’re a first-time home owner, the bank will give you a `108%` bond. The `8%` is to cover these costs. If you’re buying your second property, they expect you to pay for these fees from the proceeds of the sale of your previous property. Make sure you understand how these fees are handled so you are prepared for a cash payment, if required. These charges can be substantial.')
#####################
st.markdown('''
## How Much House Should You Buy
''')
st.markdown('Totally up to you. Banks will limit how much they are willing to lend to you based on what they think the property is worth and how much they believe you can afford.')
st.markdown('My view is making sure that the bond instalment component is not more than a third of you and your spouse’s joint income. Remember, there will still be the other incidental charges attached to home ownership that will also need to be accounted for and put into your budget.')
st.markdown('Leave yourself space to breathe.')
#####################
st.markdown('''
## How is the Bond Installment Calculated?
''')
txt3('How much are you borrowing?', 'If you **ARE NOT** putting down a deposit, this amount will be the full purchase price of the property.')
txt3('What is the interest rate?', 'You can search google for local home loan interest rates to get an idea of what number you should use. Maybe add an extra percent or two so you can get an idea of how interest relate fluctuations will affect your monthly instalment.')
txt3('Term of the bond?', 'Typically, 20 years is a good term to choose. A 30-year bond leads to a lot of interest to be paid over the term of the loan, where a 10-year bond could make the monthly repayments unaffordable.')
txt3('When does the loan start?', 'This one is less important, but most times the best time to get into the market is as soon as possible. If you cannot afford to buy what you like, rather buy what you can afford. The first property can become a stepping stone to securing the dream home you deserve.')

#####################
st.markdown('''
## Home Loan Calculator
''')
st.markdown('I have built a home loan/mortgage calculator for you.')
st.markdown('Once there, insert your mortgage parameters as discussed in the previous section. Once done, close the sidebar.')
st.markdown('The calculator will then visualise the bond for you and give you the information you need to make an informed decision.')

#####################
# Centre Mortage Calculator Button
col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button('Calculator')#todo: add link to button and align Center

txt4('Banco Central', 'The Central Bank of Brazil is Brazil`s central bank. It was established on December 31, 1964. The bank is not linked to any ministry, currently being autonomous. Like other central banks, the Brazilian central bank is the principal monetary authority of the country.','https://www.bcb.gov.br/en')
txt4('Central Bank of Russia', 'The Central Bank of the Russian Federation, also known as the Bank of Russia, is the central bank of the Russian Federation, originally founded in 1860 as the State Bank of the Russian Empire.','https://www.cbr.ru/eng/')
txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')
txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')
txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')

#####################
st.markdown('''
## Open Secrets of Home Ownership
''')
st.markdown('**Open secret number `1`**')
st.markdown('- When you buy the house, you start to build equity in the property. Over the years the property generally increases in value and the bond amount owed decreases as you make your monthly repayments. You may find that you have managed to save a substantial amount of money over five or ten years simply by owning the property you live in.')
st.markdown('**Open secret number `2`**')
st.markdown('- If you’re a tenant, you’re paying for someone else’s bond. Stands to reason. Tenants usually have a clause in their rental agreement that says they will pay more every year to rent the same home. Rent goes up `10%` every year, but the house didn’t get `10%` bigger, did it?')

#####################
st.markdown('''
## Why Do Properties Increase in Value Anyway?
''')
st.markdown('In my opinion, the reason that property values increase so much over a short period of time is because demand outstrips supply. The demand for homes is more than what is available in the market, and every day there is a bidding war going on to secure property as new buyers come into the market and as real estate investors rally to purchase more.')
st.markdown('The second major reason is inflation. The textbook description of inflated is “the erosion of the buying power of capital over time”. In others words, money is losing its purchasing power over time and this is why everything becomes more expensive as the years march on.')
st.markdown('Property is a hedge against the falling purchasing power of fiat currencies like the money we get paid at work. Truly, cash is trash.')

#####################
st.markdown('''
## Why People Don't Buy Property Sooner?
''')
txt3('Lack of information', 'They just don’t teach this stuff in school. Don’t ask me why. I didn’t make the rules. However, if you’ve managed to read this far, that excuse has gone out the window. You have the information now.')
txt3('People think they can’t afford it', 'Bond calculations are done using financial formulas to arrive at the premium breakdowns. The average person cannot just break out a financial calculator or excel spreadsheet and work it out. This reason no longer applies to you as you now have access to an interactive calculator that crunches the numbers for you!')
txt3('Bad credit record', 'Most times your credit isn’t really as bad as you think it is. The bank also regularly shows leniency because they want your business and the loan is secured with the property anyway, so worst case they can sell the house to get their money back. Don’t you make the call for the bank that you won’t get the bond. Send in your application and let the bank decide. When I got my bond, I wouldn’t have given myself the bond. It is better to be rejected than to not have attempted at all.')
txt3('Apathy, fear and procrastination', 'Some people just don’t care. Life’s more comfortable at mom’s house I suppose. Don’t let that be you. Parents develop a new found respect for you when you live in your own home. Believe me. Some people are scared to death that the bank will reject them… others are afraid of making such a big commitment. Twenty years just sounds like such a big commitment… you’re going to need a place to stay anyway, right? You may as well own it. Others still have the habit of putting important things off till tomorrow. Always tomorrow. You fast forward twenty years and they’ve paid off a bond on a property they don’t even own. It’s a recipe for disaster.')
txt3('No credit record', 'Sometimes you find yourself as an entrepreneur operating in a cash only environment. Speak with the bank to find out how to can build a record that will satisfy them that your cash flows are strong enough to qualify for a bond. These people will gladly help you with a bank account and facilities to get you started on building a credit record.')
txt3('No income to speak of', 'If you’re not working, well then, your first steps are pretty self-evident and fall outside the scope of this post. However, there’s a property at almost every income point. It might not be a property you may want to live in but it does represent an opportunity to get into the property market as a landlord and investor, and if managed properly, could become a building block to acquiring the home, lifestyle and financial freedom you deserve.')

#####################
st.markdown('''
## About the Author?
''')
st.markdown('My name is Edward. I’m a software engineer with a background in finance and engineering. I have a passion for new solutions to everyday problems. I get excited about data science, automation and robotics, machine learning and building stuff… just because.')
st.markdown('You can find me at this link:')
st.markdown('https://www.monatemedia.com/')