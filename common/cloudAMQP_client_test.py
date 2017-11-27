from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = 'amqp://gdvchttf:mzm-5BUHv34sY4qT1NTQqxE5SCM-G5Ph@sidewinder.rmq.cloudamqp.com/gdvchttf'
TEST_QUEUE_NAME = 'test'

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sentMsg = {'test': 'test'}
    client.sendMessage(sentMsg)
    receivedMsg = client.getMessage()

    assert sentMsg == receivedMsg
    print 'test_basic passed.'

if __name__ == '__main__':
    test_basic()
