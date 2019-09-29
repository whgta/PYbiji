# MongoDB
- 在mongo中，数据库和集合都不需要手动创建，当我们创建文档时，
如果文档所在的集合或者数据库不存在会自动创建数据库和集合

- 基本指令
    - show dbs
    - show databases：显示当前所有数据库
    - use 数据库名：进入指定的数据库中
    - db：表示的时当前所处的数据库
    - show collections：显示数据库中所有的集合
    
- 数据库的CRUD（增删改查）的操作
    - 向数据库插入文档
        - db.<collection>.insert(doc)
        - 向集合中插入一个文档
        - 例子：向test数据库中的，stus集合中插入一个新的学生对象
            
                {name:"wh",age:18}
                db.stus.insert({name:"wh",age:18}) 
    - db.<collection>.find()：
        - 查询当前集合中的所有的文档  
        
## 加
- 向集合插入多个文档需要用到列表
- 当我们向集合中插入文档时，如果没有给文档指定_id属性，则数据库会自动为文档添加id
    该属性用来作为文档的唯一标识
- _id我们可以自己指定，如果我们自己指定，系统就不会自动生成，但是也要唯一

                db.stus.insert([
                        {name:"lz",age:18},
                        {name:"lh",age:19},
                        ]);    
                db.stus.find(); 
                
                

##查询
- db.collection.find()
- find()用来查询集合中所有符合条件的文档
- find()可以接受一个对象作为条件参数
- find({}):{}表示所有文档
- {属性:值}：查询属性时指定值的文档
- find()返回的是一个数组
        
- db.collection.findOne()
- 用来查询集合中符合条件的第一个文档
- 返回的时一个文档对象
- db.collection.find({}).count(); 
- 查询所有结果的数量
       
       
                db.stus.find({age:17});        
                db.stus.find({age:17,name:"wh"});  
                db.stus.findOne({age:17}).name;
                
                
##修改
- db.collection.update(查询条件，新对象)
- update()默认情况下会使用新对象替换旧的对象
- 如果需要修改指定的属性，而不是替换，需要使用“修改操作符”来完成修改
    - $set 可以用了来修改文档中指定属性
    - $unset 可以用来删除一个属性 

        
        db.stus.update(
            {name:"wh"},{$set:{age:25}}    
        );        
        db.stus.find({});



##删除
- db.collection.remove()
- 删除符合条件的所有文档
    - 如果remove()第二个参数传递一个true，则只会删除一个
- 如果只传递一个空的参数，删除集合中所有的文档，但是时一个一个删除

- db.collection.drop()
- 删除一个集合
        
          
        db.stus.find({});
        db.stus.remove({name:"lh"});
        db.stus.remove({name:"lh"},true);
 