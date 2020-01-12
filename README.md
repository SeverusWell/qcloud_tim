[![PyPI](https://img.shields.io/pypi/v/wechatpy.svg)](https://pypi.org/project/wechatpy)

```
 ______     ______     __         ______     __  __     _____    
/\  __ \   /\  ___\   /\ \       /\  __ \   /\ \/\ \   /\  __-.  
\ \ \/\_\  \ \ \____  \ \ \____  \ \ \/\ \  \ \ \_\ \  \ \ \/\ \ 
 \ \___\_\  \ \_____\  \ \_____\  \ \_____\  \ \_____\  \ \____- 
  \/___/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/____/ 
                                         ______   __     __    __    
                                      /\__  _\ /\ \   /\ "-./  \   
                                      \/_/\ \/ \ \ \  \ \ \-./\ \  
                                         \ \_\  \ \_\  \ \_\ \ \_\ 
                                          \/_/   \/_/   \/_/  \/_/ 
```


QCloud TIM SDK for Python
==


> A package for qcloud im(tim), Implement REST API.
>
> 腾讯云 IM 服务 SDK.

### 功能特性

- 群组管理
- 帐号管理
- 单聊消息
- 资料管理
- 关系链管理
- 运营管理
- 消息记录

### 安装

```
pip install qcloud-tim
```



### 使用示例

```
from qcloud_tim import TimClient

tim_client = TimClient(
    app_id=os.environ.get('APP_ID') or '',
    app_key=os.environ.get('APP_KEY') or ''
)

# 获取 App 中的所有群组
result = tim_client.group_open_http_svc.get_app_id_group_list()
```



### 全部示例

```

# 单个帐号导入接口
result = tim_client.im_open_login_svc.account_import(identifier='user1', nick='nick_user0', face_url='face_url_user0')

# 批量帐号导入接口
result = tim_client.im_open_login_svc.im_open_login_svc(accounts=['user1', 'user2'])

# 帐号删除接口
result = tim_client.im_open_login_svc.account_delete(delete_item=['user1', 'user2'])

# 帐号检查接口
result = tim_client.im_open_login_svc.account_check(check_item=['user0', 'user1'])

# 帐号登录态失效接口
result = tim_client.im_open_login_svc.kick(identifier='user0')

# 单发单聊消息(文本)
result = tim_client.open_im.send_text_msg(to_account='user0', content='hi', from_account='user1')

# 批量发单聊消息(文本)
result = tim_client.open_im.batch_send_text_msg(to_account=['user0', 'user2'], content='hi', from_account='user1')

# 导入单聊消息
result = tim_client.open_im.batch_send_text_msg(to_account=['user0', 'user2'], content='hi', from_account='user1')

# 导入单聊消息
result = tim_client.open_im.import_text_msg(to_account='user0', from_account='user1', content='hi')

# 撤回单聊消息
result = tim_client.open_im.admin_msg_withdraw(to_account='user1', from_account='user0', msg_key='msg_key')

# 获取用户在线状态
result = tim_client.open_im.query_state(to_account=['user0', 'user1'])

# 拉取资料
result = tim_client.profile.portrait_get(to_account=['user0'])

# 设置资料
result = tim_client.profile.portrait_set(
    from_account=['user2'], profile_item=[{'Tag': "Tag_Profile_IM_Nick", "Value": "MyNickName"}])

# 添加好友
result = tim_client.sns.friend_add(
    from_account='user0', add_friend_item=[
        {
            "To_Account": "user1",
            "Remark": "remark1",
            "GroupName": "同学",
            "AddSource": "AddSource_Type_XXXXXXXX",
            "AddWording": "I'm Test1"
        }
    ])

# 导入好友
result = tim_client.sns.friend_import(
    from_account='user0',
    add_friend_item=[
        {
            "To_Account": "user1",
            "Remark": "remark1",
            "RemarkTime": 1420000001,
            "GroupName": ["朋友"],
            "AddSource": "AddSource_Type_XXXXXXXX",
            "AddWording": "I'm Test1",
            "AddTime": 1420000001,
            # "CustomItem":
            #     [
            #         {
            #             "Tag": "Tag_SNS_Custom_XXXX",
            #             "Value": "Test"
            #         },
            #         {
            #             "Tag": "Tag_SNS_Custom_YYYY",
            #             "Value": 0
            #         }
            #     ]
        }
    ])

# 更新好友
result = tim_client.sns.friend_update(
    from_account='user0',
    update_item=[
        {
            "To_Account": "user1",
            "SnsItem":
                [
                    {
                        "Tag": "Tag_SNS_IM_Remark",
                        "Value": "remark1"
                    }
                ]
        }
    ])

# 删除好友
result = tim_client.sns.friend_delete(from_account='user0', to_account=['user1'])

# 删除所有好友
result = tim_client.sns.friend_delete_all(from_account='user0')

# 校验好友
result = tim_client.sns.friend_check(from_account='user0', to_account=['user1', 'user2'])

# 拉取好友
result = tim_client.sns.friend_get(from_account='user0')

# 拉取指定好友(拉取指定好友的好友数据和资料数据)
result = tim_client.sns.friend_get_list(from_account='user0', to_account=['user1'])

# 添加黑名单
result = tim_client.sns.black_list_add(from_account='user0', to_account=['user1'])

# 删除黑名单
result = tim_client.sns.black_list_delete(from_account='user0', to_account=['user1'])

# 拉取黑名单
result = tim_client.sns.black_list_get(from_account='user0')

# 校验黑名单
result = tim_client.sns.black_list_check(from_account='user0', to_account=['user1'])

# 添加分组
result = tim_client.sns.group_add(from_account='user0', group_name=["group3"])

# 删除分组
result = tim_client.sns.group_delete(from_account='user0', group_name=["group2"])

# 获取 App 中的所有群组
result = tim_client.group_open_http_svc.get_app_id_group_list()

# 创建群组
result = tim_client.group_open_http_svc.create_group(
    name='group1', owner_account='user0', group_type=GroupOpenHttpSVC.TYPE_PUBLIC)

# 获取群组详细资料
result = tim_client.group_open_http_svc.get_group_info(group_id_list=['@TGS#2K5TLVDGB'])

# 获取群组成员详细资料
result = tim_client.group_open_http_svc.get_group_member_info(group_id='@TGS#2K5TLVDGB')

# 修改群组基础资料
result = tim_client.group_open_http_svc.modify_group_base_info(group_id='@TGS#2K5TLVDGB', name='new name')

# 增加群组成员
result = tim_client.group_open_http_svc.add_group_member(
    group_id='@TGS#2K5TLVDGB',
    member_list=[
        {'Member_Account': 'user1'},
        {'Member_Account': 'user2'}
    ])

# 删除群组成员
result = tim_client.group_open_http_svc.delete_group_member(
    group_id='@TGS#2K5TLVDGB',
    member_to_del_account=['user1'])

# 修改群成员资料
result = tim_client.group_open_http_svc.modify_group_member_info(
    group_id='@TGS#2K5TLVDGB',
    member_account='user1',
    role=GroupOpenHttpSVC.ROLE_ADMIN,
    msg_flag=GroupOpenHttpSVC.MSG_FLAG_ACCEPT_AND_NOTIFY,
    name_card='name_card_user1',
    shut_up_time=None
)

# 解散群组
result = tim_client.group_open_http_svc.destroy_group(group_id='@TGS#2K5TLVDGB')

# 获取用户所加入的群组
result = tim_client.group_open_http_svc.get_joined_group_list(member_account='user0')

# 查询用户在群组中的身份
result = tim_client.group_open_http_svc.get_role_in_group(group_id='@TGS#2NQBXZDG6', user_account=['user0', 'user2'])

# 批量禁言和取消禁言
result = tim_client.group_open_http_svc.forbid_send_msg(
    group_id='@TGS#2NQBXZDG6', members_account=['user0'], shut_up_time=10)

# 获取群组被禁言用户列表
result = tim_client.group_open_http_svc.get_group_shut_uin(group_id='@TGS#2NQBXZDG6')

# 在群组中发送普通消息
result = tim_client.group_open_http_svc.send_group_msg(
    group_id='@TGS#2NQBXZDG6',
    msg_body=[{
        "MsgType": "TIMTextElem",
        "MsgContent": {
            "Text": "Test text."
        }
    }])

# 在群组中发送系统通知
result = tim_client.group_open_http_svc.send_group_system_notification(group_id='@TGS#2NQBXZDG6', content='Content.')

# 撤回群组消息
result = tim_client.group_open_http_svc.group_msg_recall(group_id='@TGS#2NQBXZDG6', msg_seq_list=[{'MsgSeq': 1}])

# 转让群组
result = tim_client.group_open_http_svc.change_group_owner(group_id='@TGS#2NQBXZDG6', new_owner_account='user0')

# 导入群基础资料
result = tim_client.group_open_http_svc.import_group(name='group X')

# 导入群消息
result = tim_client.group_open_http_svc.import_group_msg(
    group_id='@TGS#2NQBXZDG6',
    msg_list=[{
        'From_Account': 'user0',
        'SendTime': int(time.time()),
        'Random': random.randint(0, 4294967295),
        'MsgBody': [  # 消息体，由一个 element 数组组成，详见 TIMMessage 消息对象
            {
                "MsgType": "TIMTextElem",  # 文本
                "MsgContent": {
                    "Text": "Text test."
                }
            }
        ]}])

# 导入群成员
result = tim_client.group_open_http_svc.import_group_member(
    group_id='@TGS#2NQBXZDG6',
    member_list=[
        {
            "Member_Account": "user1",
            "Role": GroupOpenHttpSVC.ROLE_ADMIN,
        }
    ])

# 设置成员未读消息计数
result = tim_client.group_open_http_svc.set_unread_msg_num(
    group_id='@TGS#2NQBXZDG6', member_account='user0', unread_msg_num=5)

# 删除指定用户发送的消息
result = tim_client.group_open_http_svc.delete_group_msg_by_sender(group_id='@TGS#2NQBXZDG6', sender_account='user0')

# 拉取群漫游消息
result = tim_client.group_open_http_svc.group_msg_get_simple(group_id='@TGS#2NQBXZDG6', req_msg_number=10)

# 设置全局禁言
result = tim_client.open_config_svr.set_no_speaking(
    to_account='user0', c2c_msg_no_speaking_time=10, group_msg_no_speaking_time=100)

# 查询全局禁言
result = tim_client.open_config_svr.get_no_speaking(get_account='user0')

# 查询全局禁言
result = tim_client.open_config_svr.get_app_info()

# 下载消息记录
result = tim_client.open_msg_svc.get_history(chat_type=OpenMSGSVC.CHAT_TYPE_GROUP)
```



### 问题反馈

使用 [GitHub Issues](https://github.com/SeverusWell/qcloud_tim/issues) 进行问题追踪和反馈。


###  References
- [官方文档](https://cloud.tencent.com/product/im/developer)
- [jxtech/wechatpy](https://github.com/jxtech/wechatpy)




### License 
---
This work is released under the MIT license. A copy of the license is provided in the LICENSE file.


