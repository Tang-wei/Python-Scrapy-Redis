#coding:utf-8
import MySQLdb
import redis
import json

def main():
    try:
        rediscli = redis.StrictRedis(host='192.168.2.111',port=6379,db=0,)
        mysqlcli = MySQLdb.connect(host='39.106.56.181',user='root',db='job',port=3306,passwd='123456',charset='utf8')
    except Exception,e:
        print '连接错误'
        print str(e)
        exit()

    while True:
        source,data = rediscli.blpop(["zhaopin:items"])
        print source   #redis 里的建
        print data   #redis 里的数据
        item = json.loads(data)

        try:
            #使用cursor创建游标
            cur = mysqlcli.cursor()
            #使用execute执行sql语句
            sql = "insert into  job51(position,salary,company,location,time,job_duty,url) values('%s','%s','%s','%s','%s','%s','%s') on duplicate key update "\
                  "position=values(position),salary=values(salary),company=values(company),location=values(location),time=values(time),job_duty=values(job_duty),url=values(url)" % (item['gangwei'],item['pay'],item['company'],item['site'],item['times'],item['miaoshu'],item['url'],)

            #执行sql语句
            cur.execute(sql)
            #提交sql事五
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
        except Exception,e:
            print '插入失败！'
            print str(e)
            #exit()

if __name__ == '__main__':
    main()