benchmarks = [
    {'symbol': 'SPY', 'ER': 0.12},
    {'symbol': 'AGG', 'ER': 0.05}
]

portfolio = [
    # GROWTH STOCKS
    {'symbol': 'AMD',  'bench': 'SPY', 'G': 1},  # AMD
    {'symbol': 'ADSK', 'bench': 'SPY', 'G': 1},  # Autodesk
    {'symbol': 'CMG',  'bench': 'SPY', 'G': 1},  # Chipotle
    {'symbol': 'EW',   'bench': 'SPY', 'G': 1},  # Edwards Lifescience
    {'symbol': 'LULU', 'bench': 'SPY', 'G': 1},  # Lululemon
    {'symbol': 'CRM',  'bench': 'SPY', 'G': 1},  # Salseforce
    {'symbol': 'SQ',   'bench': 'SPY', 'G': 1},  # Square
    # VALUE STOCKS
    {'symbol': 'MMM',  'bench': 'SPY', 'V': 1},  # 3M
    {'symbol': 'BAC',  'bench': 'SPY', 'V': 1},  # Bank of America
    {'symbol': 'BIIB', 'bench': 'SPY', 'V': 1},  # Biogen
    {'symbol': 'CAT',  'bench': 'SPY', 'V': 1},  # Catapillar
    {'symbol': 'CSCO', 'bench': 'SPY', 'V': 1},  # Cisco
    {'symbol': 'COP',  'bench': 'SPY', 'V': 1},  # Conoco Philips
    {'symbol': 'EMR',  'bench': 'SPY', 'V': 1},  # Emerson
    {'symbol': 'GILD', 'bench': 'SPY', 'V': 1},  # Gilead
    {'symbol': 'JNJ',  'bench': 'SPY', 'V': 1},  # Johnson and Johnson
    {'symbol': 'PEP',  'bench': 'SPY', 'V': 1},  # Pepsico
    {'symbol': 'PSA',  'bench': 'SPY', 'V': 1},  # Public Storage
    {'symbol': 'HD',   'bench': 'SPY', 'V': 1},  # Home Depot
    # DEBT/BONDS/FI
    # Investment Grade Corp. Bonds
    {'symbol': 'LQD',  'bench': 'AGG', 'D': 1},  # Inv. Grade Corp Bonds
    {'symbol': 'HYG',  'bench': 'AGG', 'D': 1},  # High Yield Corp. Bonds
    {'symbol': 'TIP',  'bench': 'AGG', 'D': 1},  # TIPs
    {'symbol': 'GOVT', 'bench': 'AGG', 'D': 1},  # US Treasury Bonds
    {'symbol': 'MUB',  'bench': 'AGG', 'D': 1},  # Muni Bonds
    {'symbol': 'VMBS', 'bench': 'AGG', 'D': 1},  # Morgage Backed
]
