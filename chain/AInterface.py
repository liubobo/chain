# coding: utf-8
from core.myIo import *
import string,os
from core import UIReform
import sys
reload(sys)

sys.setdefaultencoding('utf8')

# simulate(u'uibutton *bb;\nuibutton *bb\nuibutton *bb\nuibutton *bb\n@property (nonatomic, strong) UIButton *bxx;')

for ui in   UIReform.gen_uis():

    if ui.type == 'UIButton':
        s = ''' 
        ${name} = [UIButton km_makeButton:^(KMButtonMaker *make) {

        make.titleForState(<#(nullable NSString *)#>, UIControlStateNormal).textFont(kFont15).addTargetAndActionForControlEvents(self, @selector(${tname}ButtonTouchUpInside:), UIControlEventTouchUpInside).frame(frame(<#CGRect frame#>)).backgroundColor([UIColor redColor]).addToSuperView(<#(nonnull UIView *)#>).addMasorny(^(MASConstraintMaker *maker) {

        });
        }]
        '''
        s = string.Template(s).safe_substitute({'name': '_'+ui.name if ui.isProp else ui.name,'tname':ui.name})


    if ui.type == 'UILabel':
        s = '''
                [UILabel km_makeLabel:^(KMLabelMaker *make){
        
        make.font(kFont15).tintColor([UIColor redColor]).frame(<#CGRect frame#>).addToSuperView(<#UIView *superView#>);

    }];
              '''
        s = string.Template(s).safe_substitute(
            {'name': '_' + ui.name if ui.isProp else ui.name, 'tname': ui.name, 'type': ui.type})


    if ui.type == 'UIImageView':
        s = '''     [UIImageView km_makeImageView: ^ (KMImageViewMaker * make)
        {
            make.image( <#UIImage *image#>).frame(<#CGRect frame#>).addToSuperView(<#UIView *superView#>);;
        }];
                   '''
        s = string.Template(s).safe_substitute(
            {'name': '_' + ui.name if ui.isProp else ui.name, 'tname': ui.name, 'type': ui.type})

    else:
        s = '''
         ${name} = [ ${type} km_makeView:^(KMUIViewMaker *make) {
          make.frame(CGRectMake(<#CGFloat x#>, <#CGFloat y#>, <#CGFloat width#>, <#CGFloat height#>)).backgroundColor([UIColor redColor]).addToSuperView(<#(nonnull UIView *)#>);
        }];
        '''
        s = string.Template(s).safe_substitute({'name': '_'+ui.name if ui.isProp else ui.name,'tname':ui.name,'type':ui.type})


    print s