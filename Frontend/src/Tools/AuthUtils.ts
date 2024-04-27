import axios, { AxiosError, AxiosResponse } from "axios";
import { API_URL } from "./Globals";
import ServerError from "../Types/Errors/ServerError";

/**
 * Constructs the complete API endpoint URL by concatenating the base URL with the provided endpoint.
 * @param endpoint The endpoint to be appended to the base URL.
 * @returns The complete API endpoint URL in lowercase.
 */
function API(endpoint: string): string {
  return API_URL + endpoint.toLowerCase().toString();
}

export async function TeamLogIn(teamId: string) {
  try {
    // Send a POST request to the login endpoint of the API with the provided email and password
    const response: AxiosResponse<any> = await axios.post(API("login"), {
      teamId: teamId,
    });
    const data = response.data;
    return data;
  } catch (error: any) {
    if (error instanceof AxiosError) {
      throw new ServerError(error.message || "Couldn't log in. Server error.");
    } else {
      throw new Error("Login failed.");
    }
  }
}

export async function TrackReport(reportId: string) {
  try {
    const response: AxiosResponse<any> = await axios.get(API("report"), {
      params: { reportId: reportId },
    });
    const data = response.data;
    return data;
  } catch (error) {
    if (error instanceof AxiosError) {
      throw new ServerError(error.message || "Couldn't log in. Server error.");
    } else {
      throw new Error("Track Report failed.");
    }
  }
}
export type ReportProps = {
  userFname: string;
  userLname: string;
  potholeAddress: string;
  dangerous: boolean;
  image:string;
};
export async function CreateReport(report: ReportProps) {
  try {
    const response: AxiosResponse<any> = await axios.post(API("report"), {
      report: report,
    });
    const data = response.data;
    return data;
  } catch (error) {
    if (error instanceof AxiosError) {
      throw new ServerError(error.message || "Couldn't log in. Server error.");
    } else {
      throw new Error("Create Report failed.");
    }
  }
}
