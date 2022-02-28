class HistoryRecord(dict):

    def __init__(self, request='', response='', status='fail'):
        dict.__init__(self, request=request, response=response, status=status)
