import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

# link:https://github.com/python/cpython/blob/3.9/Lib/telnetlib.py
# doc:https://docs.python.org/3/library/telnetlib.html
# Telnet represents a connection to a Telnet server

# Telnet.read_until (expected, timeout=None)
# Đọc cho đến khi gặp một chuỗi byte nhất định, dự kiến, được gặp hoặc cho đến khi hết giây hết thời gian chờ.

# Telnet.read_all ()
# Đọc tất cả dữ liệu cho đến khi EOF dưới dạng byte; chặn cho đến khi kết nối đóng lại.

# Telnet.read_some ()
# Đọc ít nhất một byte dữ liệu đã nấu chín trừ khi EOF được nhấn. Trả về b '' nếu EOF bị đánh. Chặn nếu không có dữ liệu ngay lập tức.

# Telnet.read_very_eager ()
# Đọc mọi thứ có thể có mà không bị chặn trong I / O (háo hức).
# Tăng EOFError nếu kết nối bị đóng và không có dữ liệu nấu chín. 
# Trả về b '' nếu không có dữ liệu nấu chín. Không chặn trừ khi ở giữa một chuỗi IAC.

# Telnet.read_eager ()
# Đọc dữ liệu sẵn có.

# Telnet.read_lazy ()
# Xử lý và trả về dữ liệu đã có trong hàng đợi (lười biếng).

# Telnet.read_very_lazy ()
# Trả lại bất kỳ dữ liệu nào có sẵn trong hàng đợi đã nấu (rất lười biếng).

# Telnet.read_sb_data ()
# Trả lại dữ liệu được thu thập giữa một cặp SB / SE (phụ đề bắt đầu / kết thúc). 
# Lệnh gọi lại sẽ truy cập những dữ liệu này khi nó được gọi bằng lệnh SE. Phương pháp này không bao giờ chặn.


# Telnet.msg (msg, * args)
# In thông báo gỡ lỗi khi mức gỡ lỗi> 0. Nếu có các đối số bổ sung,
#  chúng sẽ được thay thế trong thông báo bằng cách sử dụng toán tử định dạng chuỗi tiêu chuẩn.

# Telnet.set_debuglevel (gỡ lỗi)
# Đặt mức gỡ lỗi. Giá trị của debuglevel càng cao, bạn nhận được càng nhiều đầu ra debug (trên sys.stdout).

# Telnet.close ()
# Đóng kết nối.

# Telnet.get_socket ()
# Trả lại đối tượng socket được sử dụng trong nội bộ.

# Telnet.fileno ()
# Trả lại bộ mô tả tệp của đối tượng socket được sử dụng trong nội bộ.

# Telnet.write (bộ đệm)
# Ghi một chuỗi byte vào socket, nhân đôi bất kỳ ký tự IAC nào.
#  Điều này có thể chặn nếu kết nối bị chặn. Có thể tăng OSError nếu kết nối bị đóng.


# Telnet.interact ()
# Chức năng tương tác, giả lập một ứng dụng khách Telnet rất ngu ngốc.


# Telnet.mt_interact ()
# Phiên bản đa luồng của tương tác ().

# Telnet.expect (danh sách, thời gian chờ = Không có)
# Đọc cho đến khi một từ danh sách cụm từ thông dụng khớp.