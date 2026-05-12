import express from 'express';
import setRoutes from './routes/index';

const app = express();

setRoutes(app);

app.listen(1245);

export default app;
