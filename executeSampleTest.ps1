$file = "test.txt"

Add-content -path $file -value "add random content"

git add test.txt
git commit -m "adding random content to test.txt for testing"
git push origin main