import maude

def main():
    qlock = maude.getModule('QLOCK')
    init = qlock.parseTerm('init')
    target = qlock.parseTerm('{(pc[P1]: cs) (pc[P2]: cs) OCs}')

if __name__ == "__main__":
    maude.init()
    maude.load('mutual_exclusion_protocol')

    

maude.init()
maude.load('mutual_exclusion_protocol')

qlock = maude.getModule('QLOCK')
init = qlock.parseTerm('init')
target = qlock.parseTerm('{(pc[P1]: cs) (pc[P2]: cs) OCs}')
r = init.search(1, target)
r.getRewriteCount()
r.getStateNr()

r.getStateTerm(0)
r.getStateTerm(1)