from .evidence import at
from .inspection import yield_rows
def close_period(db, known_at):
    rates={(r['payload']['product'],r['payload']['period']):r for r in at(db,'cost',known_at)}
    output=[]
    for row in yield_rows(db,known_at):
        period=row['shift'][:7];rate=rates.get((row['product'],period))
        if row['status']!='已检验' or rate is None:
            output.append({'batch':row['batch'],'status':'成本或检验待核'});continue
        unit=rate['payload']['unit_cost']
        output.append({'batch':row['batch'],'period':period,'accepted':row['accepted'],'waste_cost':(row['produced']-row['accepted'])*unit,'sources':[row['source'],row['inspection_source'],rate['digest']]})
    return output
