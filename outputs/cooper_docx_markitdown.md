git@git.xiaojukeji.com:maps-global/road-data-manager.git灵犀sdk升级

最新commit：94651b3e

disf&ofs 支持

参考cr <https://eng.xiaojukeji.com/group/39513/service/35750/cr/5830743>

1. 需要各服务自己进行disf的init 比如：disf::Scheduler::GetInstance()->InitWithFile("./disf.yaml"); 或者l1s的init。 且需要在灵犀sdk初始化前
2. 将disf名称，协议传到参数里 options.qualifier = disf\_qualifier; options.proto = proto; 具体值为如下 disf\_qualifier : "disf!map-normandy-route-sys-route\_data\_manager" proto : "http"
3. 原url参数建议注释掉。当设置原http\_url时，不使用disf，使用url，方便线下测试，会有警告日志输出
4. sdk 编译使用了最新的disf sdk。v1.3.1
5. sdk依赖 disf sdk的头文件 在dep.json或submodules中，将可用的disf头文件夹提到 sdk前。 如 { "module\_path" : "disf-cplus-spl", "git\_path" : "disf/disf-cplus-spl.git", "commit" : "v1.3.1" }, { "module\_path" : "its/road-data-manager", "git\_path" : "maps-global/road-data-manager.git", "commit" : "02e55d59" }
6. 链接使用自己本地已有的disf lib即可。 如果链接有问题，建议升级disf sdk。
7. pre验证，删掉自己本地data\_map下的文件，确保可以正确拉取。
8. 如果本地有 third-64-global， 那么可以不用加disf-cplus-spl
9. 依赖 yaml、metric等参考cr自行添加
10. 需要各个服务自行配置ofs路径。如果本地磁盘没有数据，将优先读取ofs，最后读取hdfs。 读取ofs不会下载到本地 设置方式 status*options.ofs\_path* = yourofspath
11. 如果不配置ofs路径，该功能不生效
12. 使用ofs时，确保使用LoadData传入的path，不在使用本地记录的，否则将无法灵活切换本地、ofs路径。
13. 自测建议：删除正确的本地路径，将路网挪到mock的ofs路径，则可以不用hdfs下载，正常启动。日志关键词ofs。

灵犀sdk去掉md5，服务自行进行md5校验cr

1. rp cr ：<https://git.xiaojukeji.com/maps-global/route-planner/compare/ba0235975f9df7b0d3029d482a579aea79641d47...462b4c7a9346b9fa2ebff7f4765af9974df7bdc0>
2. 依赖的库改动cr

ch <https://eng.xiaojukeji.com/group/39513/service/74119/cr/5961649>

sdk <https://eng.xiaojukeji.com/group/39513/service/77576/cr/6031761>

its-lib <https://eng.xiaojukeji.com/group/39513/service/58477/cr/6031673>

1. 改动点：sdk去掉了md5校验， 仅检查文件夹是否存在，各个服务自行进行md5 和文件加载。
2. 主要目的： 减少一次原先进行md5校验的一次io。与服务加载文件共用一次io。适配使用ofs路径的数据文件，且不增加耗时&内存

* 修改完确认无误，填下表格。（表格如果有未列出的，自行填加下，谢谢。）

|  |  |  |
| --- | --- | --- |
| 模块 | 负责人 | disf&ofs&自校验md5 |
| map-matcher-service | 曹靖松 |  |
| mm-dispatcher | 曹靖松 |  |
| driver-info-api | 武俊健 |  |
| spd-calc | 武俊健 |  |
| light-matcher | 武俊健 |  |
| traffic-merge | 武俊健 |  |
| traffic-publish | 武俊健 |  |
| route-eta | 刘祥程 |  |
| route-planner | 武俊健 | done |
| route-restore | 曹振楠 |  |
| island-compiler | 曹靖松 |  |
| capture-task-generator | 曹靖松 |  |
| traffic-interpreter | 曹靖松 |  |
| data-sync | huangzhiqiang |  |
| route-dwg-search-cbr |  |  |
| route-traffic | 武俊健 |  |
| Brazil-route-feature |  |  |
| route-feature | 刘祥程 |  |
| NaviGuide | zhouhuanqing |  |