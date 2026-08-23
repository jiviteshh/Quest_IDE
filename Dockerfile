# QuestIDE application image.
# Build a service target with:
#   docker build --target backend -t questide-backend .
#   docker build --target frontend -t questide-frontend .

FROM python:3.12-slim AS backend

WORKDIR /app
COPY Backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY Backend/app ./app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM node:22-alpine AS frontend-build

WORKDIR /app
COPY Frontend/frontend/package*.json ./
RUN npm ci
COPY Frontend/frontend/ ./
RUN npm run build

FROM node:22-alpine AS frontend

WORKDIR /app
ENV NODE_ENV=production
COPY --from=frontend-build /app/package*.json ./
COPY --from=frontend-build /app/.next ./.next
COPY --from=frontend-build /app/public ./public
COPY --from=frontend-build /app/node_modules ./node_modules
COPY --from=frontend-build /app/next.config.ts ./next.config.ts

EXPOSE 3000
CMD ["npm", "run", "start"]
