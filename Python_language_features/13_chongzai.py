"""
函数重载是为了解决两个问题：
1、可变参数的类型
2、可变参数的个数
基本的设计原则是：仅仅当两个函数除了参数类型和参数个数不同以外，
其他功能是完全相同的，此时使用函数重载。若两个函数的功能是不同的，
那么就不能使用重载，而应该使用一个名字不同的函数。
1、对于函数功能相同，但是参数类型不同，python根本不需要处理，
因为python可以接受任何类型的参数，如果函数的功能相同，那么不同的参数
类型在python中很可能是相同的代码，没有必要做成两个不同的函数
2、对于函数功能相同，参数个数不同，python做处理时，就缺省参数，对那些
缺省参数设定为缺省参数即可解决问题，因为，假设函数功能相同，那么那些缺少
的参数终归是需要用到的
对于1和2，python不需要函数重载
"""
