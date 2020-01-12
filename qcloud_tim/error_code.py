# -*- coding: utf-8 -*-
from enum import IntEnum, unique


@unique
class RESSTAPIErrorCode(IntEnum):
    """
    REST API 公共错误码，请参考 https://cloud.tencent.com/document/product/269/1519
    IM SDK 的错误码 + 服务端的错误码+ IM SDK V3 版本的错误码https://cloud.tencent.com/document/product/269/1671
    """
    # 请求包非法
    BODY_ILLEGAL_20001 = 20001

    # UserSig 或 A2 失效
    USER_SIG_OR_A2_INVALID_20002 = 20002

    # 消息发送方或接收方 UserID 无效或不存在，请检查 UserID 是否已导入即时通信 IM
    TO_ACCOUNT_OR_FROM_ACCOUNT_USER_ID_INVALID_20003 = 20003

    # 网络异常，请重试
    NETWORK_ERROR_20004 = 20004

    # 服务器内部错误，请重试
    INTERNAL_ERROR_20005 = 20005

    # 触发发送单聊消息之前回调，App 后台返回禁止下发该消息
    MESSAGE_FORBIDDEN_20006 = 20006

    # 清理关系链数据时服务器内部出错，请稍后重试
    INTERNAL_ERROR_WHEN_DELETE_30006 = 30006

    # 清理关系链数据时服务器内部超时，请稍后重试
    INTERNAL_ERROR_WHEN_DELETE_30007 = 30007

    # 并发写关系链数据触发写冲突，建议使用批量方式
    CONFLICT_WHEN_DELETE_30008 = 30008

    # 40001	请求参数错误，请根据错误描述检查请求参数
    BODY_INVALID_40001 = 40001

    # 请求参数错误，没有指定 To_Account
    BODY_TO_ACCOUNT_INVALID_40002 = 40002

    # 请求的用户帐号不存在
    USER_NOT_EXIST_40003 = 40003

    # 请求需要 App 管理员权限
    PERMISSIONS_LIMITED_40004 = 40004

    # 资料字段中包含敏感词
    CONTAINED_SENSITIVE_WORD_40005 = 40005

    # 设置资料时服务器内部错误，请稍后重试
    INTERNAL_ERROR_40006 = 40006

    # 资料字段的 Value 长度超过500字节
    VALUE_TOO_LONG_40601 = 40601
    # HTTP 解析错误 ，请检查 HTTP 请求 URL 格式
    HTTP_PARSER_ERROR_60002 = 60002

    # HTTP 请求 JSON 解析错误，请检查 JSON 格式
    BODY_JSON_PARSER_ERROR_60003 = 60003

    # 请求 URL 或 JSON 包体中帐号或签名错误
    REQUEST_AUTHENTICATION_ERROR_60004 = 60004

    # 请求 URL 或 JSON 包体中帐号或签名错误
    REQUEST_AUTHENTICATION_ERROR_60005 = 60005

    # SDKAppID 失效，请核对 SDKAppID 有效性
    SDK_APP_ID_INVALID_60006 = 60006

    # REST 接口调用频率超过限制，请降低请求频率
    REST_API_INVOKE_LIMITED_60007 = 60007

    # 服务请求超时或 HTTP 请求格式错误，请检查并重试
    REQUEST_TIMEOUT_OR_METHOD_ERROR_60008 = 60008

    # 请求资源错误，请检查请求 URL
    RESOURCE_ERROR_60009 = 60009

    # 请求需要 App 管理员权限
    PERMISSIONS_LIMITED_60010 = 60010

    # 请求频率超限，请降低请求频率
    SDK_APP_ID_INVOKE_LIMITED_60011 = 60011

    # REST 接口需要带 SDKAppID，请检查请求 URL 中的 SDKAppID
    SDK_APP_ID_REQUIRE_60012 = 60012

    # HTTP 响应包 JSON 解析错误
    RESPONSE_JSON_DECODE_ERROR_60013 = 60013

    # 置换帐号超时
    ACCOUNT_SWAP_TIMEOUT_60014 = 60014

    # 请求包体帐号类型错误，请确认帐号为字符串格式
    BODY_ACCOUNT_TYPE_ERROR_60015 = 60015

    # 请求删除的  不存在，请确认 UserID 的合法性
    USER_ID_NOT_EXIST_70107 = 70107

    # 服务端内部超时，请稍后重试
    INTERNAL_TIMEOUT_70169 = 70169

    # 服务端内部超时，请稍后重试
    INTERNAL_ERROR_70202 = 70202

    # 帐号数超限。如需创建多于100个帐号，请将应用升级为专业版，具体操作指引请参见 购买指引
    NUMBER_OF_ACCOUNTS_LIMITED_70398 = 70398

    # 参数非法，请检查必填字段是否填充，或者字段的填充是否满足协议要求
    PARAM_ILLEGAL_70402 = 70402

    # 请求失败，需要 App 管理员权限
    PERMISSIONS_LIMITED_70403 = 70403

    # 服务器内部错误，请稍后重试
    INTERNAL_ERROR_70500 = 70500

    # 删除帐号失败。仅支持删除体验版帐号，您当前应用为专业版，暂不支持帐号删除
    ACCOUNT_DELETE_FAIL_71000 = 71000

    # 消息文本安全打击
    MESSAGE_TEXT_SECURITY_STRIKE_80001 = 80001

    # JSON 格式解析失败，请检查请求包是否符合 JSON 规范
    BODY_JSON_PARSER_ERROR_90001 = 90001

    # JSON 格式请求包中 MsgBody 不符合消息格式描述，或者 MsgBody 不是 Array 类型，请参考 TIMMsgElement 对象 的定义
    BODY_MSG_BODY_INVALID_90002 = 90002

    # JSON 格式请求包体中缺少 To_Account 字段或者 To_Account 字段不是 String 类型
    BODY_TO_ACCOUNT_INVALID_90003 = 90003

    # JSON 格式请求包体中缺少 MsgRandom 字段或者 MsgRandom 字段不是 Integer 类型
    BODY_MSG_RANDOM_INVALID_90005 = 90005

    # JSON 格式请求包体中 MsgTimeStamp 字段不是 Integer 类型
    BODY_MSG_TIMESTAMP_INVALID_90006 = 90006

    # JSON 格式请求包体中 MsgBody 类型不是 Array 类型，请将其修改为 Array 类型
    BODY_MSG_BODY_INVALID_90007 = 90007

    # JSON 格式请求包体中缺少 From_Account 字段，或者From_Account 不存在。
    BODY_FROM_ACCOUNT_INVALID_90008 = 90008

    # 请求需要 App 管理员权限
    PERMISSIONS_LIMITED_90009 = 90009

    # JSON 格式请求包不符合消息格式描述，请参考 TIMMsgElement 对象 的定义
    BODY_TIM_MSG_ELEMENT_INVALID_90010 = 90010

    # 批量发消息目标帐号超过500，请减少 To_Account 中目标帐号数量
    NUMBER_OF_TO_ACCOUNT_LIMITED_90011 = 90011

    # To_Account 没有注册或不存在，请确认 To_Account 是否导入即时通信 IM 或者是否拼写错误
    BODY_TO_ACCOUNT_INVALID_90012 = 90012

    # 消息离线存储时间错误（最多不能超过7天）
    BODY_MSG_LIFETIME_INVALID_90026 = 90026

    # JSON 格式请求包体中缺少 SyncFromOldSystem 字段或者 SyncFromOldSystem 字段不是 Integer 类型
    BODY_SYNC_FROM_OLD_SYSTEM_INVALID_90030 = 90030

    # JSON 格式请求包体中 SyncOtherMachine 字段不是 Integer 类型
    BODY_SYNC_OTHER_MACHINE_INVALID_90031 = 90031

    # JSON 格式请求包体中 MsgLifeTime 字段不是 Integer 类型
    BODY_MSG_LIFETIME_INVALID_90044 = 90044

    # 请求的用户帐号不存在
    ACCOUNT_NOT_EXIST_90048 = 90048

    # 撤回请求中的 MsgKey 不合法
    BODY_MSG_KEY_INVALID_90054 = 90054

    # 服务内部错误，请重试；
    # 如果所有请求都返回该错误码，且 App 配置了第三方回调，请检查 App 服务器是否正常向即时通信 IM 后台服务器返回回调结果
    INTERNAL_ERROR_90992 = 90992

    # 服务内部错误，请重试
    INTERNAL_ERROR_90994 = 90994

    # 服务内部错误，请重试
    INTERNAL_ERROR_90995 = 90995

    # 服务内部错误，请重试
    INTERNAL_ERROR_91000 = 91000

    # JSON 数据包超长，消息包体请不要超过 8k
    BODY_TOO_LONG_93000 = 93000
