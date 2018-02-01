Rules = {'24': ('Pair', ['values', "'('", 'Values', "')'"]), '25': ('Pairs', ['Pairs', 'Pair']), '26': ('Pairs', ['Pair']), '27': ('toks', ['toks', "','", 'Token']), '20': ('Pair', ['Token', "'('", 'Expr', "')'", "'{'", 'Pairs', "'}'"]), '21': ('Pair', ['Token', "'('", "')'", "'{'", 'Pairs', "'}'"]), '22': ('Pair', ['values', "'('", 'Values', "')'", "';'"]), '23': ('Pair', ['values', "':'", 'Values', "';'"]), '28': ('toks', ['Token']), '29': ('Exprs', ['Expr', "','", 'Expr']), '0': ('$accept', ['libraries', '$end']), '4': ('Items', ['Items', 'Item']), '8': ('Token', ['token']), '59': ('cell_item', ['Statetable']), '58': ('cell_item', ['Ff']), '55': ('cell_item', ['Pair']), '54': ('cell_items', ['cell_item']), '57': ('cell_item', ['Pin']), '56': ('cell_item', ['Bus']), '51': ('Expr', ['values']), '50': ('Expr', ["'!'", 'Token']), '53': ('cell_items', ['cell_items', 'cell_item']), '52': ('Cell', ['cell', "'('", 'tuken', "')'", "'{'", 'cell_items', "'}'"]), '88': ('bus_item', ['Timing']), '89': ('bus_item', ['Pin']), '82': ('timing_items', ['timing_item']), '83': ('timing_item', ['Pair']), '80': ('Timing', ['timing', "'('", "')'", "'{'", 'timing_items', "'}'"]), '81': ('timing_items', ['timing_items', 'timing_item']), '86': ('bus_items', ['bus_item']), '87': ('bus_item', ['Pair']), '84': ('Bus', ['bus', "'('", 'tuken', "')'", "'{'", 'bus_items', "'}'"]), '85': ('bus_items', ['bus_items', 'bus_item']), '3': ('Library', ['library', "'('", 'tuken', "')'", "'{'", 'Items', "'}'"]), '7': ('Item', ['Pair']), '39': ('Expr', ['String']), '38': ('Expr', ['Number']), '33': ('Value', ['Number']), '32': ('Value', ['Floating']), '31': ('Value', ['String']), '30': ('Exprs', ['Expr']), '37': ('Expr', ['Token']), '36': ('Expr', ['ff']), '35': ('Values', ['Value']), '34': ('Values', ['Values', "','", 'Value']), '60': ('cell_item', ['Latch']), '61': ('cell_item', ['Test_cell']), '62': ('test_cell_item', ['Pin']), '63': ('test_cell_item', ['Ff']), '64': ('test_cell_item', ['Latch']), '65': ('test_cell_items', ['test_cell_items', 'test_cell_item']), '66': ('test_cell_items', ['test_cell_item']), '67': ('Pin', ['pin', "'('", 'Token', "')'", "'{'", 'pin_items', "'}'"]), '68': ('Pin', ['pin', "'('", 'Token', "','", 'Token', "')'", "'{'", 'pin_items', "'}'"]), '69': ('Pin', ['pin', "'('", 'Token', "','", 'Token', "','", 'Token', "')'", "'{'", 'pin_items', "'}'"]), '2': ('libraries', ['Library']), '6': ('Item', ['Cell']), '11': ('Floating', ['floating']), '10': ('Number', ['number']), '13': ('tuken', ['String']), '12': ('tuken', ['Token']), '15': ('Pair', ['Token', "':'", 'Number', 'Token', "';'"]), '14': ('Pair', ['Token', "':'", 'Expr', "';'"]), '17': ('Pair', ['Token', "'('", 'Expr', "','", 'Expr', "')'", "';'"]), '16': ('Pair', ['Token', "'('", 'Expr', "')'", "';'"]), '19': ('Pair', ['Token', "'('", 'Expr', "','", 'Expr', "','", 'Expr', "')'", "';'"]), '18': ('Pair', ['Token', "'('", 'Expr', "','", 'Expr', "')'"]), '48': ('Expr', ['Expr', "'-'", 'Expr']), '49': ('Expr', ["'-'", 'Number']), '46': ('Expr', ['Expr', "'+'", 'Expr']), '47': ('Expr', ["'-'", 'Floating']), '44': ('Expr', ['timing']), '45': ('Expr', ['Expr', "'*'", 'Expr']), '42': ('Expr', ['cell']), '43': ('Expr', ['pin']), '40': ('Expr', ['Floating']), '41': ('Expr', ['library']), '1': ('libraries', ['libraries', 'Library']), '5': ('Items', ['Item']), '9': ('String', ['string']), '77': ('Statetable', ['statetable', "'('", 'Exprs', "')'", "'{'", 'Pairs', "'}'"]), '76': ('Ff', ['ff', "'('", 'toks', "')'", "'{'", 'Pairs', "'}'"]), '75': ('pin_item', ['Timing']), '74': ('pin_item', ['Pair']), '73': ('pin_items', ['pin_item']), '72': ('pin_items', ['pin_items', 'pin_item']), '71': ('Pin', ['pin', "'('", 'Token', "'['", 'Number', "':'", 'Number', "']'", "')'", "'{'", 'pin_items', "'}'"]), '70': ('Pin', ['pin', "'('", 'Token', "'['", 'Number', "']'", "')'", "'{'", 'pin_items', "'}'"]), '79': ('Test_cell', ['test_cell', "'('", "')'", "'{'", 'test_cell_items', "'}'"]), '78': ('Latch', ['latch', "'('", 'toks', "')'", "'{'", 'Pairs', "'}'"])}
States = {'165': [('reduce', '$default', '67')], '133': [('shift', ':', '152'), ('shift', ']', '153')], '132': [('shift', ')', '150'), ('shift', ',', '151')], '131': [('shift', 'timing', '145'), ('shift', 'token', '7'), ('shift', 'values', '15'), ('goto', 'Token', '18'), ('goto', 'Pair', '146'), ('goto', 'pin_items', '147'), ('goto', 'pin_item', '148'), ('goto', 'Timing', '149')], '130': [('reduce', '$default', '19')], '137': [('shift', 'token', '7'), ('shift', 'values', '15'), ('goto', 'Token', '18'), ('goto', 'Pair', '71'), ('goto', 'Pairs', '160')], '136': [('shift', '*', '63'), ('shift', '+', '64'), ('shift', '-', '65'), ('reduce', '$default', '29')], '135': [('shift', 'token', '7'), ('shift', 'values', '15'), ('goto', 'Token', '18'), ('goto', 'Pair', '71'), ('goto', 'Pairs', '159')], '134': [('shift', 'pin', '80'), ('shift', 'timing', '145'), ('shift', 'token', '7'), ('shift', 'values', '15'), ('goto', 'Token', '18'), ('goto', 'Pair', '154'), ('goto', 'Pin', '155'), ('goto', 'Timing', '156'), ('goto', 'bus_items', '157'), ('goto', 'bus_item', '158')], '139': [('shift', 'token', '7'), ('shift', 'values', '15'), ('goto', 'Token', '18'), ('goto', 'Pair', '71'), ('goto', 'Pairs', '161')], '138': [('reduce', '$default', '27')], '166': [('reduce', '$default', '72')], '24': [('reduce', '$default', '3')], '25': [('reduce', '$default', '4')], '26': [('shift', 'library', '37'), ('shift', 'cell', '38'), ('shift', 'pin', '39'), ('shift', 'timing', '40'), ('shift', 'token', '7'), ('shift', 'number', '29'), ('shift', 'string', '8'), ('shift', 'floating', '30'), ('shift', 'ff', '41'), ('shift', 'values', '42'), ('shift', ')', '43'), ('shift', '-', '44'), ('shift', '!', '45'), ('goto', 'Token', '46'), ('goto', 'String', '47'), ('goto', 'Number', '48'), ('goto', 'Floating', '49'), ('goto', 'Expr', '50')], '27': [('shift', 'library', '37'), ('shift', 'cell', '38'), ('shift', 'pin', '39'), ('shift', 'timing', '40'), ('shift', 'token', '7'), ('shift', 'number', '29'), ('shift', 'string', '8'), ('shift', 'floating', '30'), ('shift', 'ff', '41'), ('shift', 'values', '42'), ('shift', '-', '44'), ('shift', '!', '45'), ('goto', 'Token', '46'), ('goto', 'String', '47'), ('goto', 'Number', '51'), ('goto', 'Floating', '49'), ('goto', 'Expr', '52')], '20': [('reduce', '$default', '6')], '21': [('shift', 'token', '7'), ('shift', 'string', '8'), ('goto', 'Token', '9'), ('goto', 'String', '10'), ('goto', 'tuken', '28')], '22': [('shift', 'number', '29'), ('shift', 'string', '8'), ('shift', 'floating', '30'), ('goto', 'String', '31'), ('goto', 'Number', '32'), ('goto', 'Floating', '33'), ('goto', 'Value', '34'), ('goto', 'Values', '35')], '23': [('shift', 'number', '29'), ('shift', 'string', '8'), ('shift', 'floating', '30'), ('goto', 'String', '31'), ('goto', 'Number', '32'), ('goto', 'Floating', '33'), ('goto', 'Value', '34'), ('goto', 'Values', '36')], '160': [('shift', 'token', '7'), ('shift', 'values', '15'), ('shift', '}', '174'), ('goto', 'Token', '18'), ('goto', 'Pair', '96')], '28': [('shift', ')', '53')], '29': [('reduce', '$default', '10')], '161': [('shift', 'token', '7'), ('shift', 'values', '15'), ('shift', '}', '175'), ('goto', 'Token', '18'), ('goto', 'Pair', '96')], '0': [('shift', 'library', '1'), ('goto', 'libraries', '2'), ('goto', 'Library', '3')], '4': [('shift', 'token', '7'), ('shift', 'string', '8'), ('goto', 'Token', '9'), ('goto', 'String', '10'), ('goto', 'tuken', '11')], '8': [('reduce', '$default', '9')], '163': [('reduce', '$default', '65')], '119': [('shift', ';', '130')], '120': [('shift', '{', '131')], '121': [('shift', 'token', '7'), ('goto', 'Token', '132')], '122': [('shift', 'number', '29'), ('goto', 'Number', '133')], '123': [('shift', '{', '134')], '124': [('shift', '{', '135')], '125': [('shift', 'library', '37'), ('shift', 'cell', '38'), ('shift', 'pin', '39'), ('shift', 'timing', '40'), ('shift', 'token', '7'), ('shift', 'number', '29'), ('shift', 'string', '8'), ('shift', 'floating', '30'), ('shift', 'ff', '41'), ('shift', 'values', '42'), ('shift', '-', '44'), ('shift', '!', '45'), ('goto', 'Token', '46'), ('goto', 'String', '47'), ('goto', 'Number', '48'), ('goto', 'Floating', '49'), ('goto', 'Expr', '136')], '126': [('shift', '{', '137')], '127': [('shift', 'token', '7'), ('goto', 'Token', '138')], '128': [('shift', '{', '139')], '129': [('shift', 'pin', '80'), ('shift', 'ff', '83'), ('shift', 'latch', '84'), ('goto', 'test_cell_item', '140'), ('goto', 'test_cell_items', '141'), ('goto', 'Pin', '142'), ('goto', 'Ff', '143'), ('goto', 'Latch', '144')], '167': [('shift', 'timing', '145'), ('shift', 'token', '7'), ('shift', 'values', '15'), ('goto', 'Token', '18'), ('goto', 'Pair', '146'), ('goto', 'pin_items', '177'), ('goto', 'pin_item', '148'), ('goto', 'Timing', '149')], '118': [('shift', '{', '129')], '59': [('reduce', '$default', '47')], '58': [('reduce', '$default', '49')], '55': [('shift', 'number', '29'), ('shift', 'string', '8'), ('shift', 'floating', '30'), ('goto', 'String', '31'), ('goto', 'Number', '32'), ('goto', 'Floating', '33'), ('goto', 'Value', '70')], '54': [('shift', ';', '69'), ('reduce', '$default', '24')], '57': [('shift', 'token', '7'), ('shift', 'values', '15'), ('goto', 'Token', '18'), ('goto', 'Pair', '71'), ('goto', 'Pairs', '72')], '56': [('reduce', '$default', '23')], '51': [('shift', 'token', '7'), ('goto', 'Token', '66'), ('reduce', '$default', '38')], '50': [('shift', ')', '61'), ('shift', ',', '62'), ('shift', '*', '63'), ('shift', '+', '64'), ('shift', '-', '65')], '53': [('shift', '{', '68')], '52': [('shift', ';', '67'), ('shift', '*', '63'), ('shift', '+', '64'), ('shift', '-', '65')], '164': [('shift', ')', '176')], '179': [('shift', ')', '184')], '195': [('shift', 'timing', '145'), ('shift', 'token', '7'), ('shift', 'values', '15'), ('shift', '}', '196'), ('goto', 'Token', '18'), ('goto', 'Pair', '146'), ('goto', 'pin_item', '166'), ('goto', 'Timing', '149')], '194': [('reduce', '$default', '69')], '178': [('shift', '{', '183')], '191': [('reduce', '$default', '70')], '190': [('shift', 'timing', '145'), ('shift', 'token', '7'), ('shift', 'values', '15'), ('goto', 'Token', '18'), ('goto', 'Pair', '146'), ('goto', 'pin_items', '195'), ('goto', 'pin_item', '148'), ('goto', 'Timing', '149')], '193': [('reduce', '$default', '81')], '192': [('reduce', '$default', '80')], '115': [('reduce', '$default', '28')], '114': [('shift', ',', '125'), ('shift', '*', '63'), ('shift', '+', '64'), ('shift', '-', '65'), ('reduce', '$default', '30')], '88': [('reduce', '$default', '54')], '89': [('reduce', '$default', '57')], '111': [('shift', ')', '120'), ('shift', ',', '121'), ('shift', '[', '122')], '110': [('shift', ')', '119'), ('shift', '*', '63'), ('shift', '+', '64'), ('shift', '-', '65')], '113': [('shift', ')', '124')], '112': [('shift', ')', '123')], '82': [('shift', '(', '102')], '83': [('shift', '(', '103')], '80': [('shift', '(', '100')], '81': [('shift', '(', '101')], '86': [('reduce', '$default', '55')], '87': [('shift', 'pin', '80'), ('shift', 'bus', '81'), ('shift', 'token', '7'), ('shift', 'statetable', '82'), ('shift', 'ff', '83'), ('shift', 'latch', '84'), ('shift', 'test_cell', '85'), ('shift', 'values', '15'), ('shift', '}', '106'), ('goto', 'Token', '18'), ('goto', 'Pair', '86'), ('goto', 'cell_item', '107'), ('goto', 'Pin', '89'), ('goto', 'Ff', '90'), ('goto', 'Statetable', '91'), ('goto', 'Latch', '92'), ('goto', 'Test_cell', '93'), ('goto', 'Bus', '94')], '84': [('shift', '(', '104')], '85': [('shift', '(', '105')], '3': [('reduce', '$default', '2')], '177': [('shift', 'timing', '145'), ('shift', 'token', '7'), ('shift', 'values', '15'), ('shift', '}', '182'), ('goto', 'Token', '18'), ('goto', 'Pair', '146'), ('goto', 'pin_item', '166'), ('goto', 'Timing', '149')], '7': [('reduce', '$default', '8')], '108': [('reduce', '$default', '20')], '109': [('reduce', '$default', '17')], '102': [('shift', 'library', '37'), ('shift', 'cell', '38'), ('shift', 'pin', '39'), ('shift', 'timing', '40'), ('shift', 'token', '7'), ('shift', 'number', '29'), ('shift', 'string', '8'), ('shift', 'floating', '30'), ('shift', 'ff', '41'), ('shift', 'values', '42'), ('shift', '-', '44'), ('shift', '!', '45'), ('goto', 'Token', '46'), ('goto', 'String', '47'), ('goto', 'Number', '48'), ('goto', 'Floating', '49'), ('goto', 'Exprs', '113'), ('goto', 'Expr', '114')], '103': [('shift', 'token', '7'), ('goto', 'Token', '115'), ('goto', 'toks', '116')], '100': [('shift', 'token', '7'), ('goto', 'Token', '111')], '101': [('shift', 'token', '7'), ('shift', 'string', '8'), ('goto', 'Token', '9'), ('goto', 'String', '10'), ('goto', 'tuken', '112')], '106': [('reduce', '$default', '52')], '107': [('reduce', '$default', '53')], '104': [('shift', 'token', '7'), ('goto', 'Token', '115'), ('goto', 'toks', '117')], '105': [('shift', ')', '118')], '39': [('reduce', '$default', '43')], '38': [('reduce', '$default', '42')], '33': [('reduce', '$default', '32')], '32': [('reduce', '$default', '33')], '31': [('reduce', '$default', '31')], '30': [('reduce', '$default', '11')], '37': [('reduce', '$default', '41')], '36': [('shift', ';', '56'), ('shift', ',', '55')], '35': [('shift', ')', '54'), ('shift', ',', '55')], '34': [('reduce', '$default', '35')], '176': [('shift', '{', '181')], '60': [('reduce', '$default', '50')], '61': [('shift', '{', '73'), ('shift', ';', '74')], '62': [('shift', 'library', '37'), ('shift', 'cell', '38'), ('shift', 'pin', '39'), ('shift', 'timing', '40'), ('shift', 'token', '7'), ('shift', 'number', '29'), ('shift', 'string', '8'), ('shift', 'floating', '30'), ('shift', 'ff', '41'), ('shift', 'values', '42'), ('shift', '-', '44'), ('shift', '!', '45'), ('goto', 'Token', '46'), ('goto', 'String', '47'), ('goto', 'Number', '48'), ('goto', 'Floating', '49'), ('goto', 'Expr', '75')], '63': [('shift', 'library', '37'), ('shift', 'cell', '38'), ('shift', 'pin', '39'), ('shift', 'timing', '40'), ('shift', 'token', '7'), ('shift', 'number', '29'), ('shift', 'string', '8'), ('shift', 'floating', '30'), ('shift', 'ff', '41'), ('shift', 'values', '42'), ('shift', '-', '44'), ('shift', '!', '45'), ('goto', 'Token', '46'), ('goto', 'String', '47'), ('goto', 'Number', '48'), ('goto', 'Floating', '49'), ('goto', 'Expr', '76')], '64': [('shift', 'library', '37'), ('shift', 'cell', '38'), ('shift', 'pin', '39'), ('shift', 'timing', '40'), ('shift', 'token', '7'), ('shift', 'number', '29'), ('shift', 'string', '8'), ('shift', 'floating', '30'), ('shift', 'ff', '41'), ('shift', 'values', '42'), ('shift', '-', '44'), ('shift', '!', '45'), ('goto', 'Token', '46'), ('goto', 'String', '47'), ('goto', 'Number', '48'), ('goto', 'Floating', '49'), ('goto', 'Expr', '77')], '65': [('shift', 'library', '37'), ('shift', 'cell', '38'), ('shift', 'pin', '39'), ('shift', 'timing', '40'), ('shift', 'token', '7'), ('shift', 'number', '29'), ('shift', 'string', '8'), ('shift', 'floating', '30'), ('shift', 'ff', '41'), ('shift', 'values', '42'), ('shift', '-', '44'), ('shift', '!', '45'), ('goto', 'Token', '46'), ('goto', 'String', '47'), ('goto', 'Number', '48'), ('goto', 'Floating', '49'), ('goto', 'Expr', '78')], '66': [('shift', ';', '79')], '67': [('reduce', '$default', '14')], '68': [('shift', 'pin', '80'), ('shift', 'bus', '81'), ('shift', 'token', '7'), ('shift', 'statetable', '82'), ('shift', 'ff', '83'), ('shift', 'latch', '84'), ('shift', 'test_cell', '85'), ('shift', 'values', '15'), ('goto', 'Token', '18'), ('goto', 'Pair', '86'), ('goto', 'cell_items', '87'), ('goto', 'cell_item', '88'), ('goto', 'Pin', '89'), ('goto', 'Ff', '90'), ('goto', 'Statetable', '91'), ('goto', 'Latch', '92'), ('goto', 'Test_cell', '93'), ('goto', 'Bus', '94')], '69': [('reduce', '$default', '22')], '175': [('reduce', '$default', '78')], '174': [('reduce', '$default', '76')], '173': [('reduce', '$default', '77')], '172': [('reduce', '$default', '85')], '171': [('reduce', '$default', '84')], '170': [('shift', '{', '180')], '181': [('shift', 'token', '7'), ('shift', 'values', '15'), ('goto', 'Token', '18'), ('goto', 'Pair', '186'), ('goto', 'timing_items', '187'), ('goto', 'timing_item', '188')], '182': [('reduce', '$default', '68')], '183': [('shift', 'timing', '145'), ('shift', 'token', '7'), ('shift', 'values', '15'), ('goto', 'Token', '18'), ('goto', 'Pair', '146'), ('goto', 'pin_items', '189'), ('goto', 'pin_item', '148'), ('goto', 'Timing', '149')], '180': [('shift', 'timing', '145'), ('shift', 'token', '7'), ('shift', 'values', '15'), ('goto', 'Token', '18'), ('goto', 'Pair', '146'), ('goto', 'pin_items', '185'), ('goto', 'pin_item', '148'), ('goto', 'Timing', '149')], '2': [('shift', '$end', '5'), ('shift', 'library', '1'), ('goto', 'Library', '6')], '162': [('reduce', '$default', '79')], '187': [('shift', 'token', '7'), ('shift', 'values', '15'), ('shift', '}', '192'), ('goto', 'Token', '18'), ('goto', 'Pair', '186'), ('goto', 'timing_item', '193')], '184': [('shift', '{', '190')], '6': [('reduce', '$default', '1')], '186': [('reduce', '$default', '83')], '188': [('reduce', '$default', '82')], '189': [('shift', 'timing', '145'), ('shift', 'token', '7'), ('shift', 'values', '15'), ('shift', '}', '194'), ('goto', 'Token', '18'), ('goto', 'Pair', '146'), ('goto', 'pin_item', '166'), ('goto', 'Timing', '149')], '196': [('reduce', '$default', '71')], '185': [('shift', 'timing', '145'), ('shift', 'token', '7'), ('shift', 'values', '15'), ('shift', '}', '191'), ('goto', 'Token', '18'), ('goto', 'Pair', '146'), ('goto', 'pin_item', '166'), ('goto', 'Timing', '149')], '99': [('shift', 'library', '37'), ('shift', 'cell', '38'), ('shift', 'pin', '39'), ('shift', 'timing', '40'), ('shift', 'token', '7'), ('shift', 'number', '29'), ('shift', 'string', '8'), ('shift', 'floating', '30'), ('shift', 'ff', '41'), ('shift', 'values', '42'), ('shift', '-', '44'), ('shift', '!', '45'), ('goto', 'Token', '46'), ('goto', 'String', '47'), ('goto', 'Number', '48'), ('goto', 'Floating', '49'), ('goto', 'Expr', '110')], '98': [('shift', ';', '109'), ('reduce', '$default', '18')], '168': [('shift', ')', '178')], '169': [('shift', ']', '179')], '91': [('reduce', '$default', '59')], '90': [('reduce', '$default', '58')], '93': [('reduce', '$default', '61')], '92': [('reduce', '$default', '60')], '95': [('reduce', '$default', '21')], '94': [('reduce', '$default', '56')], '97': [('shift', 'token', '7'), ('shift', 'values', '15'), ('shift', '}', '108'), ('goto', 'Token', '18'), ('goto', 'Pair', '96')], '96': [('reduce', '$default', '25')], '11': [('shift', ')', '12')], '10': [('reduce', '$default', '13')], '13': [('shift', 'cell', '14'), ('shift', 'token', '7'), ('shift', 'values', '15'), ('goto', 'Items', '16'), ('goto', 'Item', '17'), ('goto', 'Token', '18'), ('goto', 'Pair', '19'), ('goto', 'Cell', '20')], '12': [('shift', '{', '13')], '15': [('shift', '(', '22'), ('shift', ':', '23')], '14': [('shift', '(', '21')], '17': [('reduce', '$default', '5')], '16': [('shift', 'cell', '14'), ('shift', 'token', '7'), ('shift', 'values', '15'), ('shift', '}', '24'), ('goto', 'Item', '25'), ('goto', 'Token', '18'), ('goto', 'Pair', '19'), ('goto', 'Cell', '20')], '19': [('reduce', '$default', '7')], '18': [('shift', '(', '26'), ('shift', ':', '27')], '117': [('shift', ')', '128'), ('shift', ',', '127')], '116': [('shift', ')', '126'), ('shift', ',', '127')], '151': [('shift', 'token', '7'), ('goto', 'Token', '168')], '150': [('shift', '{', '167')], '153': [('shift', ')', '170')], '152': [('shift', 'number', '29'), ('goto', 'Number', '169')], '155': [('reduce', '$default', '89')], '154': [('reduce', '$default', '87')], '157': [('shift', 'pin', '80'), ('shift', 'timing', '145'), ('shift', 'token', '7'), ('shift', 'values', '15'), ('shift', '}', '171'), ('goto', 'Token', '18'), ('goto', 'Pair', '154'), ('goto', 'Pin', '155'), ('goto', 'Timing', '156'), ('goto', 'bus_item', '172')], '156': [('reduce', '$default', '88')], '159': [('shift', 'token', '7'), ('shift', 'values', '15'), ('shift', '}', '173'), ('goto', 'Token', '18'), ('goto', 'Pair', '96')], '158': [('reduce', '$default', '86')], '48': [('reduce', '$default', '38')], '49': [('reduce', '$default', '40')], '46': [('reduce', '$default', '37')], '47': [('reduce', '$default', '39')], '44': [('shift', 'number', '29'), ('shift', 'floating', '30'), ('goto', 'Number', '58'), ('goto', 'Floating', '59')], '45': [('shift', 'token', '7'), ('goto', 'Token', '60')], '42': [('reduce', '$default', '51')], '43': [('shift', '{', '57')], '40': [('reduce', '$default', '44')], '41': [('reduce', '$default', '36')], '1': [('shift', '(', '4')], '5': [('accept', '$default', 0)], '9': [('reduce', '$default', '12')], '146': [('reduce', '$default', '74')], '147': [('shift', 'timing', '145'), ('shift', 'token', '7'), ('shift', 'values', '15'), ('shift', '}', '165'), ('goto', 'Token', '18'), ('goto', 'Pair', '146'), ('goto', 'pin_item', '166'), ('goto', 'Timing', '149')], '144': [('reduce', '$default', '64')], '145': [('shift', '(', '164')], '142': [('reduce', '$default', '62')], '143': [('reduce', '$default', '63')], '140': [('reduce', '$default', '66')], '141': [('shift', 'pin', '80'), ('shift', 'ff', '83'), ('shift', 'latch', '84'), ('shift', '}', '162'), ('goto', 'test_cell_item', '163'), ('goto', 'Pin', '142'), ('goto', 'Ff', '143'), ('goto', 'Latch', '144')], '148': [('reduce', '$default', '73')], '149': [('reduce', '$default', '75')], '77': [('shift', '*', '63'), ('shift', '+', '64'), ('shift', '-', '65'), ('reduce', '$default', '46')], '76': [('shift', '*', '63'), ('shift', '+', '64'), ('shift', '-', '65'), ('reduce', '$default', '45')], '75': [('shift', ')', '98'), ('shift', ',', '99'), ('shift', '*', '63'), ('shift', '+', '64'), ('shift', '-', '65')], '74': [('reduce', '$default', '16')], '73': [('shift', 'token', '7'), ('shift', 'values', '15'), ('goto', 'Token', '18'), ('goto', 'Pair', '71'), ('goto', 'Pairs', '97')], '72': [('shift', 'token', '7'), ('shift', 'values', '15'), ('shift', '}', '95'), ('goto', 'Token', '18'), ('goto', 'Pair', '96')], '71': [('reduce', '$default', '26')], '70': [('reduce', '$default', '34')], '79': [('reduce', '$default', '15')], '78': [('shift', '*', '63'), ('shift', '+', '64'), ('shift', '-', '65'), ('reduce', '$default', '48')]}