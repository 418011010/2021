from xml.dom import minidom
with open('dom_write.xml','r',encoding='utf8') as fh:
  # parse()获取DOM对象
  dom=minidom.parse(fh)
  # 获取根节点
  bookstore=dom.documentElement
  #节点名称
  print(bookstore.nodeName)
  #获取某个节点下所有子节点，是个列表
  print(bookstore.childNodes)
  #通过dom对象或根元素，再根据标签名获取元素节点，是个列表
  books=bookstore.getElementsByTagName('book')
  print(books)
  book_cata=[]
  for b in books:
    if b.hasAttribute('category'):
      print(b.getAttribute('category'))
      book_cata.append(b.getAttribute('category'))
    print(b.getElementsByTagName('price')[0].childNodes[0].data)
  print(book_cata)
  


