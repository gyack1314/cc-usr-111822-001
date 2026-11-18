from .evidence import at
def batches(db, known_at):
    result=[]
    for row in at(db,'batch',known_at):
        p=row['payload']
        if p['produced']<0 or p['scrapped']<0 or p['scrapped']>p['produced']:
            raise ValueError('批次产量无效')
        result.append({'batch':row['id'],'line':p['line'],'product':p['product'],'supplier':p['supplier'],'shift':p['shift'],'produced':p['produced'],'scrapped':p['scrapped'],'source':row['digest']})
    return result
