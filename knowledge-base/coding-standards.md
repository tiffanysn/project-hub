# 通用编码与 Git 规范 📐

在所有子项目中遵循统一的规范，有助于代码维护和与 AI 结对编程。

---

## 1. Git 提交规范 (Conventional Commits)

每次提交建议使用以下前缀：
- `feat:` 新增功能 (feature)
- `fix:` 修复 bug
- `docs:` 文档更新
- `refactor:` 代码重构（不改变现有行为）
- `chore:` 辅助工具、依赖变动或构建流程修改
- `test:` 添加或修改测试用例

*示例：*
```text
feat(auth): add login with google oauth
fix(api): handle null pointer in user profile response
docs: update readme with quickstart guide
```

---

## 2. 命名规范
- **文件命名**：推荐小写中划线（kebab-case，例如 `user-profile.js`）或下划线（snake_case）。
- **函数/变量**：小驼峰（camelCase，例如 `fetchUserData`）。
- **类名/组件**：大驼峰（PascalCase，例如 `UserProfileCard`）。
- **常量**：大写下划线（UPPER_CASE，例如 `API_BASE_URL`）。

---

## 3. 环境变量与安全
- **严禁**将私钥、API Keys、密码等敏感数据提交到 Git 仓库。
- 本地配置统一写在 `.env` 或 `.env.local` 中，并已在根目录 `.gitignore` 中忽略。
- 提供 `.env.example` 展示所需变量格式。
