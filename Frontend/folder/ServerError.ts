class ServerError extends Error {
  constructor(msg: string) {
    super(msg);
    Object.setPrototypeOf(this, ServerError.prototype);
  }
}

export default ServerError;
