import os
from presenter import presenter


if __name__ == '__main__':
    port = int(os.getenv('PORT'), '5000')
    presenter.run(host='0.0.0.0', port=port)


