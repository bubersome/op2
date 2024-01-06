# ZeroTier与Tailscale技术比较

发表于[2022年7月18日](https://pfschina.org/wp/?p=9141)

随着现代企业迁移到基于云的服务和远程工作，加固的企业围墙正在恶化，传统VPN的使用也是如此。网络架构师正在采用新的“零信任”方法，这意味着物理网络不可信，并且每个设备都必须始终进行端到端加密和身份验证。

人们希望能够以高度安全的方式从任何地方连接到私有资源，这就是ZeroTier和Tailscale的用武之地。

下图显示了传统VPN与Tailscale的区别。

[![img](https://pfschina.org/wp/wp-content/uploads/2022/07/36697-scaled.jpg)](https://pfschina.org/wp/wp-content/uploads/2022/07/36697-scaled.jpg)

[![img](https://pfschina.org/wp/wp-content/uploads/2022/07/33644-scaled.jpg)](https://pfschina.org/wp/wp-content/uploads/2022/07/33644-scaled.jpg)

ZeroTier是一个分散的网络虚拟化平台。他们的口号是“去中心化直到它受伤，然后集中化直到它起作用。他们提供了一个定制的协议，具有2个虚拟化层：

- 虚拟第 1 层（VL1） 是对等网络主干，用于加密通信、确保端点身份验证并使用非对称密钥验证凭证。
- 虚拟第 2 层（VL2） 建立在 VL1 之上，利用软件定义的网络原理作为虚拟可扩展局域网 （VX-LAN） 发挥作用。VL2 负责创建安全网络边界、多播、实施基于规则和功能的安全性以及基于证书的访问控制。

ZeroTier的集中式组件是一组12个根服务器，这些服务器分布在全球，提供了稳定的服务，有助于快速建立点对点连接，并保证一切正常运转。

ZeroTier的硬件无关技术适用于大多数工业、商业或个人设备。它们可以在Windows，macOS，Android，iOS，Linux，FreeBSD和NAS设备上运行。产品是开源的，但受其商业源代码许可证的约束。

相比之下，Tailscale的架构使用SaaS中央协调服务，该服务对最终用户来说是不可见的。节点通过登录到中央身份系统（如Google，Microsoft AzureAD或Okta）进行授权。Tailscale不使用自定义协议，而是使用标准的WireGuard VPN协议进行数据传输。

ZeroTier和Tailscale用途相同，但它们具有不同的底层结构。下面我们将进行全面的比较，来分析它们各自的优势和存在的差异。

文章目录



[初始设置](https://pfschina.org/wp/?p=9141#初始设置)[连接](https://pfschina.org/wp/?p=9141#连接)[安全](https://pfschina.org/wp/?p=9141#安全)[性能](https://pfschina.org/wp/?p=9141#性能)[管理](https://pfschina.org/wp/?p=9141#管理)[总结](https://pfschina.org/wp/?p=9141#总结)

# 初始设置

ZeroTier被设计为一种“零配置”技术。用户启动 ZeroTier 节点时无需写入配置文件或提供其他节点的IP地址。ZeroTier的虚拟化第 2 层 （VL2） 充当配置管理器。通过共享计算机生成的密码，可以将新节点添加到 ZeroTier 网络，该密码必须由用户在连接时输入。

Tailscale使连接设备变得简单：只需使用组织的SSO标识提供程序在每个设备上安装并登录到Tailscale即可使用。Tailscale管理密钥分发、密钥轮换、设备证书和用户的所有配置，相对来说，使用安装更方便，对技术的要求并不重要。

# 连接

ZeroTier的点对点连接可靠且快速，是因为采用了低延迟的直接通信。与Tailscale一样，ZeroTier负责NAT遍历。ZeroTier的根服务器帮助各个节点建立对等连接。如果NAT遍历失败，ZeroTier的根服务器将继续中继通信，这将导致增加延迟。

WireGuard通常需要任意连接的一端具有静态IP地址。但是，Tailscale在WireGuard顶部添加了一层按需NAT遍历，以便设备可以直接通信，甚至通过防火墙进行通信，而无需手动配置。如果无法进行NAT遍历或UDP被阻止，Tailscale会自动通过TCP（HTTPS） 中继加密流量，以便设备始终可以进行通信。它根据网络条件自动在这些不同的传输机制之间切换WireGuard。

# 安全

ZeroTier的目标是成为“零信任”网络解决方案。数据包是端到端加密的，未经授权的各方无法读取。VL1上的每个对等体都拥有一个全局唯一的40位ZeroTier地址，但与IP地址不同，这些是不透明的加密标识符，不编码任何路由信息。ZeroTier使用现代256位ECC，遵循创建它的专业密码学家制定的最佳实践。

截至目前，ZeroTier还不支持单点登录 （SSO） 或多重身份验证 （MFA）。ZeroTier用户必须使用其私钥登录，并且需要在控制平面上单独获得批准。获得授权后，每个设备的密钥将永久受信任，没有能力强制执行密钥刷新或轮换期。

Tailscale提供完整的端到端数据加密。设备的私钥永远不会离开设备，因此Tailscale无法解密网络流量。通过针对公司的SSO标识提供者进行授权，可以将新节点添加到 Tailscale 网络。默认配置会导致节点从Tailscale 网络过期，除非定期重新进行身份验证，这会触发密钥轮换。还提供可选的设备状态检查，以防止设备加入网络，除非它们得到公司策略的批准。

在Tailscale中，管理员配置中央RBAC ACL策略，以便可以精确限制网络流量。尽管管理员可以在一个中央策略中制定访问规则，但该策略被编译成一组数据包过滤器，这些过滤器由各个节点本身强制执行，从而提供零信任网络所期望的安全属性。

Tailscale通过其标识提供者集成支持多重身份验证 （MFA）。

# 性能

与传统VPN相比，ZeroTier提供非常低的延迟连接，一旦建立了对等连接。现有带宽就会得到有效利用，用户很少遇到延迟问题。与Tailscale一样，ZeroTier用户遇到延迟问题的唯一情况是当对等连接被完全阻止并且必须回退到通过外部服务器进行中继时才会发生。

在大多数环境中，Tailscale的吞吐量与ZeroTier相似。从理论上讲，Tailscale使用的WireGuard协议占用的开销更低，因此延迟低于ZeroTier的协议，但在实际使用当中，这种差异并不明显。

# 管理

ZeroTier和Tailscale都提供多种定价计划，其中包含多个功能包。这两种产品都提供基于Web的仪表板，可以监视和配置网络。

# 总结

ZeroTier和Tailscale都提供点对点网状VPN技术。它们使用不同的协议来提供功能相似的服务。ZeroTier的协议是定制的，而Tailscale则使用行业标准的WireGuard协议作为其数据平面。这两种产品都提供NAT 遍历、加密的对等连接和管理仪表板。

可以预见，ZeroTier和Tailscale未来都会是传统VPN的出色替代品，并且在现代企业环境中的应用潜力无限。

[ 原文地址](https://tailscale.com/kb/1139/tailscale-vs-zerotier/)

此条目由[鉄血男兒](https://pfschina.org/wp/?author=1)发表在[OTHER](https://pfschina.org/wp/?cat=27)分类目录，并贴了[Tailscale](https://pfschina.org/wp/?tag=tailscale)标签。将[固定链接](https://pfschina.org/wp/?p=9141)加入收藏夹。