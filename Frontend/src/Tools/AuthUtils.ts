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
      // If it's an AxiosError, extract the error message from the response data
      switch (error.response?.status) {
        case 404:
          throw new Error("Report inexistant");
        case 500:
          throw new ServerError(
            error.message || "Couldn't treat request. Server error."
          );
        default:
          // If it's a generic Error, throw a default error message
          throw new Error(error.message);
      }
    } else {
      throw new Error("Track report failed");
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
      // If it's an AxiosError, extract the error message from the response data
      switch (error.response?.status) {
        case 404:
          throw new Error(
            error.message ||
              "Could not find wanted report."
          );
        case 500:
          throw new ServerError(
            error.message ||
              "Couldn't request reset password email. Server error."
          );
        default:
          // If it's a generic Error, throw a default error message
          throw new Error("Reset Password Request failed.");
      }
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
  image: string;
  email: string;
};
export async function CreateReport(report: ReportProps) {
  try {
    const response: AxiosResponse<any> = await axios.post(API("requests"), {
      report: report,
    });
    const data = response.data;
    return data;
  } catch (error) {
    if (error instanceof AxiosError) {
      // If it's an AxiosError, extract the error message from the response data
      switch (error.response?.status) {
        case 404:
          throw new Error(error.message || "Could not create report.");
        case 500:
          throw new ServerError(
            error.message ||
              "Couldn't request reset password email. Server error."
          );
        default:
          // If it's a generic Error, throw a default error message
          throw new Error("Reset Password Request failed.");
      }
    } else {
      throw new Error("Create Report failed.");
    }
  }
}

export type UpdateProps = {
  id: number;
  status: string;
};

export async function UpdateStatus(props: UpdateProps) {
  try {
    const response: AxiosResponse = await axios.put(API("requests"), {
      id: props.id,
      status: props.status,
    });
    const status = response.status;
    return status;
  } catch (error) {
    if (error instanceof AxiosError) {
      // If it's an AxiosError, extract the error message from the response data
      switch (error.response?.status) {
        case 404:
          throw new Error(error.message || "Report not found.");
        case 500:
          throw new ServerError(
            error.message ||
              "Couldn't request reset password email. Server error."
          );
        default:
          // If it's a generic Error, throw a default error message
          throw new Error("Reset Password Request failed.");
      }
    } else {
      throw new Error("Create Report failed.");
    }
  }
}
