## 1. create_ new_article

### 参数：

参数名|类型|描述
----|----|----  
title|CHAR(45)|文章标题
content|Text|文章内容 
category|Integer|文章类型id
 

### 返回值:

无

### 描述：  

用户新建文章，将文章以及相关信息添加到文章表中 ，并在缓存中建立相应数据 

## 2. delete_article  

### 参数：  
参数名|类型|描述
----|----|----
id|Integer|要删除文章的id

### 返回值  
  
无
  
### 描述：  
  
用户删除已有的文章，将文章表中的相应记录删除，并从缓存中删除相应记录  

## 3. modify_article

### 参数：

参数名|类型|描述
----|----|---- 
id|Interger|文章id 
title|CHAR(45)|文章标题
content|Text|文章内容
category|Integer|文章类型id  

### 返回值:

无

### 描述：  

用户修改文章，将文章以及相关信息更新到文章表中 ，并在缓存中更新相应数据   

## 4. read_article

### 参数：

参数名|类型|描述
----|----|---- 
id|Interger|文章id  

### 返回值:

无

### 描述：  

用户从缓存（若存在相应数据）或数据库中读取文章  

## 5. show_ article_ name_ with_ id

### 参数：

无  

### 返回值:

无

### 描述：  

显示所有文章的id和标题  

## 6. show_ all_ category_ and_ id

### 参数：

无  

### 返回值:

无

### 描述：  

显示所有文章类型过的id和名字