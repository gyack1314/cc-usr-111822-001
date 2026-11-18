from .evidence import at
from .production import batches
def yield_rows(db, known_at):
    tests={r['id']:r for r in at(db,'inspection',known_at)}
    result=[]
    for batch in batches(db,known_at):
        test=tests.get(batch['batch'])
        if not test:
            result.append({**batch,'status':'待检验'});continue
        reworked=test['payload']['reworked']
        if reworked<0 or reworked>batch['produced']-batch['scrapped']:
            raise ValueError('返修量与批次产量不符')
        accepted=batch['produced']-batch['scrapped']-reworked
        result.append({**batch,'status':'已检验','accepted':accepted,'yield_rate':accepted/batch['produced'] if batch['produced'] else None,'inspection_source':test['digest']})
    return result
