import os
from presenter import presenter
from infra.dependency_injection.inject_config import register_ioc


if __name__ == 'main':
    register_ioc()
    port = int(os.getenv('PORT'))
    presenter.run(host='0.0.0.0', port=port)


