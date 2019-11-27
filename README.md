# inner_pressure(审方性能测试脚本)

## 脚本执行步骤

1. 修改config/config.ini里的所有配置为被测服务器的配置;修改config/config.py里的FILE_PATH为实际测试文件读取路径
2. 创建并发测试需要的用户，终端下执行 python run_user.py
3. 选择multi_scenario.py中main里的locust命令，注释掉不需要的命令，终端下执行： python multi_scenario.py