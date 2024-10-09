# Chọn base image từ Python
FROM python:3.9-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép các file cần thiết vào hình ảnh
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào hình ảnh
COPY . .

# Chạy lệnh Scrapy
CMD ["scrapy", "crawl", "mycaulong"]  
